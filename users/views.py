from random import choice, randrange
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.conf.urls import url
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.gzip import gzip_page

from learning_log.settings import MAIL_PASSWORD
from .models import UserInfo
from .forms import UserRegisterForm, EmailForm, VerifyForm

def logout(request):
    """退出"""
    django_logout(request)
    return HttpResponseRedirect(reverse('about:home'))

@gzip_page
def register(request):
    """注册新用户"""
    if not request.user.is_authenticated:
        if request.method != 'POST':
            # 显示空的注册表单
            form = UserRegisterForm()
        else:
            # 处理填写好的表单
            form = UserRegisterForm(data=request.POST)

            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.email = request.POST['email']
                new_user_info = UserInfo(email=request.POST['email'], 
                    check_email=False, check_code='000000', owner=new_user)
                new_user.save()
                new_user_info.save()
                # 让用户自动登录，并重定向到邮箱验证页面
                authenticated_user = authenticate(username=new_user.username,
                    password=request.POST['password1'])
                login(request, authenticated_user)
                return HttpResponseRedirect(reverse('users:verify'))

        context = {'form':form}
        return render(request, 'users/register.html', context)
    else:
        return HttpResponseRedirect(reverse('about:home'))

@gzip_page
@login_required
def verify(request):
    """为新用户验证电子邮件地址"""
    user_info = UserInfo.objects.filter(owner=request.user)
    user_info = user_info[0]

    if user_info.check_email == False:
        if request.method == 'POST':
            # 处理填写好的表单
            if request.POST['check_code'] == user_info.check_code:
                user_info.check_email = True
                user_info.save()
                return HttpResponseRedirect(reverse('about:home'))
            else:
                return render(request, 'users/verify_error.html')
        else:
            return render(request, 'users/verify.html')
    else:
        return HttpResponseRedirect(reverse('about:home'))

    

def send_mail(request):
    """向用户发送验证邮件"""
    user_info = UserInfo.objects.filter(owner=request.user)
    user_info = user_info[0]

    if not user_info.check_email:
        try:
            user_info = UserInfo.objects.filter(owner=request.user)
            user_info = user_info[0]

            char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            verify_code = ''
            for x in range(0, randrange(5, 11)):
                verify_code += choice(char)
            user_info.check_code = verify_code
            user_info.save()

            html = '<h2>请输入 '+user_info.check_code+' 验证您的电子邮件</h2><p>如果您没有要求注册学习笔记账户，请忽略该邮件。</p><p>这是一封自动发送的邮件，无需回复。</p>'
            text = '请输入 '+user_info.check_code+' 验证您的电子邮件。\n如果您没有要求注册学习笔记账户，请忽略该邮件。\n这是一封自动发送的邮件，无需回复。'
            msg = MIMEMultipart()
            msg.attach(MIMEText(text, 'plain', 'utf-8'))
            msg.attach(MIMEText(html, 'html', 'utf-8'))
            msg['From'] = formataddr((Header('学习笔记', 'utf-8').encode(), '26922dd@sina.com'))
            msg['To'] = formataddr((Header('尊敬的学习笔记用户', 'utf-8').encode(), user_info.email))
            msg['Subject'] = Header(user_info.check_code+'是您的验证码', 'utf-8').encode()

            server = smtplib.SMTP_SSL('smtp.sina.com')
            server.starttls()
            server.set_debuglevel(1)
            server.login('26922dd@sina.com', MAIL_PASSWORD)
            server.sendmail('26922dd@sina.com', [user_info.email], msg.as_string())
            server.quit()
        except Exception as e:
            return HttpResponse("Error："+e)
        else:
            return HttpResponse("OK")
    else:
        return HttpResponse("error")
    
def username(request):
    """检查用户注册时输入内容是否有效"""
    if not request.user.is_authenticated and request.method == 'GET' and request.GET:
        for user in User.objects.all():
            if request.GET['d'] == user.username:
                return HttpResponse("false")
            else:
                return HttpResponse("true")

    else:
        return HttpResponse("error")

def verify_code(request):
    """检查用户验证电子邮件时输入内容是否有效"""
    user_info = UserInfo.objects.filter(owner=request.user)
    user_info = user_info[0]

    if request.user.is_authenticated and request.method == 'GET' and request.GET and user_info.check_email == False:
        if request.GET['d'] == user_info.check_code:
            return HttpResponse("true")
        else:
            return HttpResponse("false")
    else:
        return HttpResponse("error")
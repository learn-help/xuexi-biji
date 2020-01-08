# from random import choice, randrange
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
# import smtplib

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.conf.urls import url
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import UserInfo
from .forms import UserRegisterForm, EmailForm, VerifyForm

def logout(request):
    """退出"""
    django_logout(request)
    return HttpResponseRedirect('/')

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
                new_user = form.save()
                new_user_info = UserInfo(email='example@example.com', 
                    check_email=False, check_code='000000', owner=new_user)
                new_user_info.save()
                # 让用户自动登录，并重定向到首页
                authenticated_user = authenticate(username=new_user.username,
                    password=request.POST['password1'])
                login(request, authenticated_user)
                return HttpResponseRedirect('/topics/')

        context = {'form':form}
        return render(request, 'users/register.html', context)
    else:
        return HttpResponseRedirect('/topics/')

'''
@login_required
def email(request):
    """为新用户添加电子邮件地址"""
    user_info = UserInfo.objects.filter(owner=request.user)
    user_info = user_info[0]

    if user_info.check_email == False:
        if request.method != 'POST':
            # 显示空的注册表单
            form = EmailForm()
        else:
            # 处理填写好的表单
            form = EmailForm(data=request.POST)

            if form.is_valid():
                user_info.email = request.POST['email']
                user_info.save()
                return HttpResponseRedirect('/users/verify/')

    context = {'form':form}
    return render(request, 'users/email.html', context)


@login_required
def verify(request):
    """为新用户添加电子邮件地址"""
    user_info = UserInfo.objects.filter(owner=request.user)
    user_info = user_info[0]

    if user_info.check_email == False and user_info.email != 'example@example.com':
        if request.method != 'POST':
            # 显示空的注册表单
            form = VerifyForm()

            char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
            'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', 
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', 
            '+', '[', '{', ']', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', 
            '.', '>', '/', '?']
            verify_code = ''
            for x in range(0, randrange(5, 11)):
                verify_code += choice(char)
            user_info.check_code = verify_code

            html = '<link rel="stylesheet" href="https://xuexi-biji.herokuapp.com/static/learning_logs/bootstrap.min.css"><script src="https://xuexi-biji.herokuapp.com/static/learning_logs/jquery.min.js"></script><script src="https://xuexi-biji.herokuapp.com/static/learning_logs/bootstrap.min.js"></script><div class="container"><div class="page-header"><h2>请输入 '+user_info.check_code+' 验证您的电子邮件</h2></div><div>'
            text = '请输入 '+user_info.check_code+' 验证您的电子邮件'
            msg = MIMEMultipart('alternative')
            msg.attach(MIMEText(text, 'plain', 'utf-8'))
            msg.attach(MIMEText(html, 'html', 'utf-8'))
            msg['From'] = formataddr((Header('学习笔记', 'utf-8').encode(), 'users@xuexi-biji.herokuapp.com'))
            msg['To'] = formataddr((Header('尊敬的学习笔记用户', 'utf-8').encode(), 'user_info.email'))
            msg['Subject'] = Header(user_info.check_code+'是您的验证码', 'utf-8').encode()

            server = smtplib.SMTP('smtp.sina.com', 25)
            server.set_debuglevel(1)
            server.login('26922dd@sina.com', 'fdc2bc909389c5c7')
            server.sendmail('26922dd@sina.com', [user_info.email], msg.as_string())
            server.quit()
        else:
            # 处理填写好的表单
            form = VerifyForm(data=request.POST)

            if request.POST['check_code'] == user_info.check_code:
                user_info.check_email = True
                user_info.save()
                return HttpResponseRedirect('/topics/')
            else:
                form.errors = {'check_code': ['验证码不正确']}

    context = {'form':form}
    return render(request, 'users/verify.html', context)
'''

def register_check(request):
    """检查用户注册时输入内容是否有效"""
    if not request.user.is_authenticated and request.method == 'GET' and request.GET:
        for user in User.objects.all():
            if request.GET['d'] == user.username:
                return HttpResponse("false")
            else:
                return HttpResponse("true")

    else:
        return HttpResponseRedirect('/topics/')
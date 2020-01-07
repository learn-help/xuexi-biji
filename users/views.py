from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.conf.urls import url
from django.contrib.auth.models import User

from .models import UserInfo
from .forms import UserRegisterForm

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
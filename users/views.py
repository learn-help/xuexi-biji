from random import randrange

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.conf.urls import url

from .forms import UserRegisterForm

def view_logout(request):
    """退出"""
    logout(request)
    return HttpResponseRedirect('/')

def view_register(request):
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
        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', 
        '2', '3', '4', '5', '6', '7', '8', '9', '@', '.', '+',  '-', '_']
        i = randrange(5, 20)
        default_username = ''
        default_password = ''
        while i:
            default_username += char[randrange(1, len(char), randrange(1, 5))]
            default_password += char[randrange(1, len(char), randrange(1, 5))]
            i-=1

        check_data = {'username': default_username, 'password1': default_password, 'password2': default_password}
        if request.GET['m'] == '1':
            check_data['username'] = request.GET['d']
        elif request.GET['m'] == '2':
            check_data['password1'] = request.GET['d']
            check_data['password2'] = request.GET['d']

        form = UserRegisterForm(data=check_data)
        if form.is_valid():
            return HttpResponse("true")
        else:
            return HttpResponse("false")

    else:
        return HttpResponseRedirect('/topics/')
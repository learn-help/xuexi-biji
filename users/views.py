from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def view_logout(request):
    """退出"""
    logout(request)
    return HttpResponseRedirect('https://xuexi-biji.herokuapp.com/')

def view_register(request):
    """注册新用户"""
    if not request.user.is_authenticated:
        if request.method != 'POST':
            # 显示空的注册表单
            form = UserCreationForm()
        else:
            # 处理填写好的表单
            form = UserCreationForm(data=request.POST)

            if form.is_valid():
                new_user = form.save()
                # 让用户自动登录，并重定向到首页
                authenticated_user = authenticate(username=new_user.username,
                    password=request.POST['password1'])
                login(request, authenticated_user)
                return HttpResponseRedirect('https://xuexi-biji.herokuapp.com/topics/')

        context = {'form':form}
        return render(request, 'users/register.html', context)

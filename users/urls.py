"""为引用程序users定义URL模式"""

from django.urls import re_path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # 登录页面
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    # 退出页面
    re_path(r'^logout/$', views.view_logout, name='logout'),

    # 注册页面
    re_path(r'^register/$', views.view_register, name='register'),

    # 检查用户注册时输入内容是否有效的API
    re_path(r'^register/check/$', views.register_check, name='register_check'),
]

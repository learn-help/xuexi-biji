"""为引用程序 users 定义 URL 模式"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # 登录页面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    # 退出页面
    path('logout/', views.logout, name='logout'),

    # 注册页面
    path('register/', views.register, name='register'),

    # 验证邮箱页面
    path('verify/', views.verify, name='verify'),

    # 发送邮件
    path('send-mail/', views.send_mail, name='send_mail'),

    # 检查用户验证电子邮件时输入的内容是否有效的 API
    path('check/verify-code/', views.verify_code, name='verify_code'),

    # 检查用户注册时输入的内容是否有效的 API
    path('check/username/', views.register_check, name='register_check'),
]

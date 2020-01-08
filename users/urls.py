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

    # 输入邮箱地址页面
    # path('email/', views.email, name='email'),

    # 验证邮箱页面
    # path('verify/', views.verify, name='verify'),

    # 检查用户注册时输入内容是否有效的 API
    path('register/check/', views.register_check, name='register_check'),
]

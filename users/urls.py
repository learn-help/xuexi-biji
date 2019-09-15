"""为引用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # 登录页面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    # 退出页面
    url(r'^logout/$', views.view_logout, name='logout'),

    # 注册页面
    url(r'^register/$', views.view_register, name='register'),

    # 切换账号页面
    url(r'^other/$', views.view_other, name='other'),
]

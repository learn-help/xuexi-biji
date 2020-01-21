"""为引用程序 about 定义 URL 模式"""

from django.urls import path

from . import views

urlpatterns = [
    # 主页
    path('', views.home, name='home'),

    # test
    path('start/', views.start, name='start'),
]

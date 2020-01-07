"""为引用程序learning_logs定义URL模式"""

from django.urls import path

from . import views

urlpatterns = [
    # 主页
    path('', views.home, name='home'),

    # 所有主题页面
    path('topics/', views.topics, name='topics'),
      
    # 单个主题的详细信息页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # 单个条目的详细信息页面
    # path('topics/<int:topic_id>/<int:entry_id>/', views.entry, name='entry'),

    # 用于添加新主题的网页
    path('topics/new/', views.new_topic, name='new_topic'),

    # 用于添加新条目的网页
    path('topics/<int:topic_id>/new/', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    path('topics/<int:topic_id>/<int:entry_id>/edit/', views.edit_entry, name='edit_entry'),
]

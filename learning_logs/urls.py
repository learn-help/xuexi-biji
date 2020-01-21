"""为引用程序 learning_logs 定义 URL 模式"""

from django.urls import path

from . import views

urlpatterns = [
    # 所有主题页面
    path('', views.topics, name='topics'),
      
    # 单个主题的详细信息页面
    path('<int:topic_id>/', views.topic, name='topic'),

    # 用于添加新主题的网页
    path('new/', views.new_topic, name='new_topic'),
    
    # 单个条目的详细信息页面
    # path('<int:topic_id>/<int:entry_id>/', views.entry, name='entry'),

    # 用于添加新条目的网页
    path('<int:topic_id>/new/', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    path('<int:topic_id>/<int:entry_id>/edit/', views.edit_entry, name='edit_entry'),
]

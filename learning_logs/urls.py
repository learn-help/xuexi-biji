"""为引用程序learning_logs定义URL模式"""

from django.urls import re_path

from . import views

urlpatterns = [
    # 主页
    re_path(r'^$', views.home, name='home'),

    # javascript_error页面
    re_path(r'^js_error$', views.js_error, name='js_error'),

    # 所有主题页面
    re_path(r'^topics/$', views.topics, name='topics'),
      
    # 单个主题的详细信息页面
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 单个条目的详细信息页面
    # re_path(r'topics/(?P<topic_id>\d+)/(?P<entry_id>\d+)/$', views.entry, name='entry'),

    # 用于添加新主题的网页
    re_path(r'^topics/new/$', views.new_topic, name='new_topic'),

    # 用于添加新条目的网页
    re_path(r'^topics/(?P<topic_id>\d+)/new/$', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    re_path(r'topics/(?P<topic_id>\d+)/(?P<entry_id>\d+)/edit/$', views.edit_entry, name='edit_entry'),
]

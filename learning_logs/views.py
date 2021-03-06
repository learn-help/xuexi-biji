# import io, time

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.views.decorators.gzip import gzip_page

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from users.models import UserInfo

def check_user_have_email(user):
    user_info = UserInfo.objects.filter(owner=user)
    user_info = user_info[0]
    return user_info.check_email

@gzip_page
def topics(request):
    """显示当前用户的主题， 如果未登录返回学习笔记的主页"""
    if request.user.is_authenticated:
        user_info = UserInfo.objects.filter(owner=request.user)
        user_info = user_info[0]

        if user_info.check_email:
            topics = Topic.objects.filter(owner=request.user).order_by('date_added')
            context = {'topics': topics, }
            return render(request, 'learning_logs/topics.html', context)
        else:
            return HttpResponseRedirect(reverse('users:verify'))

    else:
        return render(request, 'learning_logs/home.html')

@gzip_page
@login_required
@user_passes_test(check_user_have_email, login_url='/users/verify/')
def topic(request, topic_id):
    """Show a single topic, and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@gzip_page
@login_required
@user_passes_test(check_user_have_email, login_url='/users/verify/')
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

@gzip_page
@login_required
@user_passes_test(check_user_have_email, login_url='/users/verify/')
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.topic = topic
            new.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)   

@gzip_page
@login_required
@user_passes_test(check_user_have_email, login_url='/users/verify/')
def edit_entry(request, topic_id, entry_id):
    """编辑既有条目"""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.date_added = timezone.now()
            edit.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)
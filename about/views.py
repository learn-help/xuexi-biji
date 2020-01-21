from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.gzip import gzip_page

@gzip_page
def home(request):
    """学生助手的主页"""
    # log_object = io.open('learning_log/static/logs', 'at')
    # print(time.time(), request.headers['User-Agent'], request.META['REMOTE_ADDR'], file=log_object, end='\n')
    return render(request, 'about/home.html')

@gzip_page
@login_required
def start(request):
    if request.user.is_staff:
        return HttpResponse("This is a test page.")
    else:
        return HttpResponse("error")
from django.contrib import admin

from users.models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'owner', 'check_email')
    list_filter = ['check_email']

admin.site.register(UserInfo, UserInfoAdmin)
from django.contrib import admin

from learning_logs.models import Topic,Entry

class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'owner', 'date_added')
    list_filter = ['date_added', 'owner']

class EntryAdmin(admin.ModelAdmin):
    list_display = ('text', 'topic', 'date_added')
    list_filter = ['date_added', 'topic']

admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)
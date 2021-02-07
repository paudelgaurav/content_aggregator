from django.contrib import admin

from .models import Topic,News

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
        list_display = ('title','source','url','topic')
        list_filter = ('topic','source')
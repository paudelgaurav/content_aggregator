from django.contrib import admin

from .models import Topic, News


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'subscribers')

    def subscribers(self, obj):
        return "\n".join([s.username for s in obj.subscriber.all()])


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'url', 'topic', )
    list_filter = ('topic', 'source', )

from rest_framework import serializers

from .models import Topic, News


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['title', 'slug', ]


class NewsSerializer(serializers.ModelSerializer):
    topic = serializers.CharField(source='topic.title')

    class Meta:
        model = News
        fields = ['title', 'content', 'url', 'source', 'topic', ]


class SubscribedTopicSerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=True)

    class Meta:
        model = Topic
        fields = ['title', 'news']

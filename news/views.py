from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import get_news
from .models import Topic
from .serializers import (
    NewsSerializer, SubscribedTopicSerializer,
    TopicSerializer
)


class TopicList(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class NewsList(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        _topic = self.kwargs['topic'].lower()
        topic = get_object_or_404(Topic, slug=_topic)
        topic.news.all().delete()
        get_news(_topic)

        return topic.news.all()


class SubscribedTopics(APIView):

    def get(self, request, *args, **kwargs):
        user = self.request.user

        if user.topics.exists():
            for topic in user.topics.all():
                topic.news.all().delete()
                get_news(topic.slug)

            serializer = SubscribedTopicSerializer(
                user.topics.all(),
                many=True
            )
            return Response(serializer.data)

        available_topics = Topic.objects.all()
        serializer = TopicSerializer(available_topics, many=True)
        return Response(
            {
                "message": "You aren't subscriber of any topics",
                "available topics": serializer.data
            }
        )


class SubscribeTopic(APIView):

    def get(self, request, format=None, topic=None):
        user = request.user
        topic_obj = get_object_or_404(Topic, slug=topic.lower())

        if topic_obj in user.topics.all():
            user.topics.remove(topic_obj)
            return Response({'subscribed': False})

        user.topics.add(topic_obj)
        return Response({'subscribed': True})

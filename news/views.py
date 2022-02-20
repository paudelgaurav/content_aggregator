from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Topic
from .serializers import (NewsSerializer, SubscribedTopicSerializer,
                          TopicSerializer)
from .utils import getNews


class TopicList(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class SubscribedTopics(APIView):

    def get(self,request, format=None):
        user = self.request.user
        subscribed_topics = user.topics.all()
        available_topics = Topic.objects.all()

        avail_topics = TopicSerializer(available_topics, many=True)
        if subscribed_topics:
            for t in subscribed_topics:
                news = t.news.all()
                if news.exists():
                    news.delete()                        
                    getNews(t.slug)           
                    topics = SubscribedTopicSerializer(subscribed_topics, many=True)
                    return Response(topics.data)
                else:
                    data = {
                            "message": "You aren't subscriber of any topics",
                            "available topics": avail_topics.data
                        }
                    return Response(data)


class NewsList(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        topic = self.kwargs['topic'].lower()
        t = get_object_or_404(Topic, slug=topic)
        news = t.news.all()
        news.delete()
        getNews(topic)
        return t.news.all()


class SubscribeTopic(APIView):
    def get(self, request, format=None, topic=None):
        user = self.request.user
        topic = topic.lower()
        t = get_object_or_404(Topic, slug=topic)
        subscribed = None
        if user.is_authenticated:
            if t in user.topics.all():
                subscribed = False
                user.topics.remove(t)
            else:
                subscribed = True
                user.topics.add(t)
                data = {'subscribed': subscribed}
                return Response(data)

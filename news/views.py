from django.shortcuts import render,get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Topic,News
from .serializers import TopicSerializer, NewsSerializer,SubscribedTopicSerializer
from .scrape import getNews

class TopicList(generics.ListAPIView):
        queryset = Topic.objects.all()
        serializer_class = TopicSerializer

class SubscribedTopics(APIView):

        def get(self,request,format=None):
                user = self.request.user
                subcribed_topics = user.topics.all()
                available_topics = Topic.objects.all()
                avail_topics = TopicSerializer(available_topics, many=True)
                if subcribed_topics:
                        topics = SubscribedTopicSerializer(subcribed_topics, many=True)
                        return Response(topics.data)
                else:
                        data = {
                                "message": "You haven't subscribe to any topics",
                                "available topics": avail_topics.data
                        }
                        return Response(data)

class NewsList(generics.ListAPIView):
        serializer_class = NewsSerializer
        
        def get_queryset(self):
                topic = self.kwargs['topic']
                t = get_object_or_404(Topic, slug=topic)
                news = t.news.all()
                news.delete()
                getNews(topic)
                queryset = t.news.all()
                return queryset



class SubscribeTopic(APIView):
        def get(self,request,format=None, topic = None):
                user = self.request.user
                t = get_object_or_404(Topic, slug=topic)
                subscribed = None
                if user.is_authenticated:
                        if t in user.topics.all():
                                subscribed = False
                                user.topics.remove(t)
                        else:
                            subscribed = True
                            user.topics.add(t)


                data = {
                        'subscribed': subscribed
                }

                return Response(data)

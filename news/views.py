from django.shortcuts import render,get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Topic,News
from .serializers import TopicSerializer, NewsSerializer
from .scrape import getNews

class TopicList(generics.ListAPIView):
        queryset = Topic.objects.all()
        serializer_class = TopicSerializer

class SubscribedTopics(APIView):

        def get(self,request,format=None):
                user = self.request.user
                topics = user.topics.all()
                t = TopicSerializer(topics, many=True)
                return Response(t.data)


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



#class SubscribedTopics(APIView):
 #       def get(self,request,format=None, topic = None):
  #              user = self.request.user
   #             subscribed = None

    #            if user.is_authenticated:


from django.urls import path,include

from .views import TopicList,NewsList,SubscribedTopics,SubscribeTopic

urlpatterns = [

    #list of all topics
    path('topics/',TopicList.as_view(),name='topic_list'),
    
    #generates news
    path('topics/<slug:topic>/',NewsList.as_view(), name='news'),
    
    #list of all subcribed contents
    path('subs/',SubscribedTopics.as_view(),name='topics'),
    
    #to subscribe
    path('subscribe/<slug:topic>/',SubscribeTopic.as_view()),

    #default drf authentication
    path('auth/',include('rest_framework.urls')),
    
    #rest_auth 3rd party package authentication
    path('accounts/',include('rest_auth.urls')),
    
    path('accounts/register/',include('rest_auth.registration.urls'))
]
from django.urls import path,include

from .views import TopicList,NewsList,SubscribedTopics,SubscribeTopic

urlpatterns = [

    path('topics/',TopicList.as_view(),name='topic_list'),
   
    path('topics/<slug:topic>/',NewsList.as_view(), name='news'),
    
    path('subs/',SubscribedTopics.as_view(),name='topics'),
    
    path('subscribe/<slug:topic>/',SubscribeTopic.as_view()),

    path('auth/',include('rest_framework.urls')),
    
    path('accounts/',include('rest_auth.urls')),
    
    path('accounts/register/',include('rest_auth.registration.urls'))
]
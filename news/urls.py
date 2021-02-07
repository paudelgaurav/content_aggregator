from django.urls import path,include

from .views import TopicList,NewsList,SubscribedTopics

urlpatterns = [

    path('',TopicList.as_view(),name='topic_list'),
    path('topic/<slug:topic>/',NewsList.as_view(), name='news'),
    path('subs/',SubscribedTopics.as_view(),name='topics'),
    path('subscribe/<slug:topic>/',SubscribedTopics.as_view()),
    path('auth/',include('rest_framework.urls')),
    path('account/',include('rest_auth.urls')),
    path('account/register/',include('rest_auth.registration.urls'))
]
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Content Aggregator",
      default_version='v1'
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),

   # api
   path('', include('news.urls')),
   # Documentation with swagger
   path(
         'docs/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'
      ),
   path(
         'redocs/',
         schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'
   ),
]

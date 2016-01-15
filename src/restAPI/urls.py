from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework import routers

from restAPI import views

#router = routers.DefaultRouter()


urlpatterns = [
    #url(r'^', include(router.urls)),
    url(r'^(?P<fichier>\D+)', views.home),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

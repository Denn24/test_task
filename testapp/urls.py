from django.conf.urls import url, include
from django.contrib import admin

from testapp.views import cesar, ajax

urlpatterns = [
    url(r'ajax', ajax),
    url(r'^$', cesar )
]
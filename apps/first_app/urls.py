from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^message$', views.message),
    url(r'^load$', views.load),
    url(r'^logout$', views.logout)
]
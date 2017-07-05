from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^reviews$', views.reviews),
]

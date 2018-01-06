from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^', TemplateView.as_view(template_name="index.html")),
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    # url(r'^reviews$', views.reviews),
    url(r'^login$', views.login),
    url(r'^create_review$', views.create_review),
    url(r'^like/(?P<id>\d+)$', views.like),
    url(r'^unlike/(?P<id>\d+)$', views.unlike),
    url(r'^account/(?P<id>\d+)$', views.account),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^add/(?P<id>\d+)$', views.add),
    url(r'^unfriend/(?P<id>\d+)$', views.unfriend),
]

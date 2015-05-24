
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$/handle_request/', views.handle_request),
    url(r'^/search/$', views.search),
]

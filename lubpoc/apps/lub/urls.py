from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cars/$', views.car_list, name='car_list'),
    url(r'^cars/(?P<car_id>[0-9]+)/', views.car_detail, name='car_detail'),
    url(r'^lubs/$', views.lub_list, name='lub_list'),
    url(r'^lubs/(?P<lub_id>[0-9]+)/', views.lub_detail, name='lub_detail'),
    url(r'^match/$', views.lub_match, name='lub_match'),
]

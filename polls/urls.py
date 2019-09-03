from django.conf.urls import url
from django.conf.urls import include, url

from polls import views

urlpatterns = [
    #url(r'^main_site/$', views.main_site),
    url(r'^vote/$', views.vote),
    url(r'^statistics/$', views.statistics),
    url(r'^vote/Restaurant_Info/(?P<rest_id>\d+)/$', views.restaurant_menu),
    url(r'^vote/thank/$', views.thank),
    url(r'^vote/registration/$', views.registration),

    url(r'^order/$', views.order),
    url(r'^order/place_order/$', views.order),

    url(r'^orders_to_go/$', views.orders_to_go),

    #testing the info of the restaurant
    #url(r'^vote/Restaurant_Info/4/$', views.restaurant_menu),
]
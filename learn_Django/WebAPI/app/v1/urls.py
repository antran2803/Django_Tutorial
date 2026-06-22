from django.urls import path
from django.contrib import admin
from app.v1.client.views import client_list,client_detail,post_list,post_detail
urlpatterns = [
 path('client/', client_list, name='client-list'),
 path('client/<int:pk>/',client_detail ,name='client-detail'),
 path('post/',post_list,name='post-list'),
 path('post/<int:pk>/',post_detail,name='post-detail'),    
]
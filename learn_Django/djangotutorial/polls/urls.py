from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name = 'home'),
    path('detail/<int:id>',views.detail_info, name = 'detail_info'),
    path('search/' , views.Search_Poll, name = 'search_Poll'),
    path('delete/<int:id>/',views.delete_info,name='delete_info'),
    path('create/',views.create_info , name = 'create_info')
]
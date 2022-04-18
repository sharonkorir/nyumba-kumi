from django.urls import path
from . import views

urlpatterns=[
  path('', views.index, name='index'),
  path('search/', views.search_results, name='search_results'),
  path('new_neighbourhood/', views.create_neighbourhood, name='new_neighbourhood'),
  path('neighbourhoods/', views.neighbourhoods, name='neighbourhoods'),
  path('join_neighbourhood/<int:pk>', views.join_neighbourhood, name='join_neighbourhood'),
  path('change_neighbourhood/<id>', views.change_neighbourhood, name='change_neighbourhood'),
  
]
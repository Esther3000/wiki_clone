from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_page, name='create_page'),
    path('<str:title>/', views.view_page, name='view_page'),
    path('wiki/search/', views.search_pages, name='search_pages'),
    
]
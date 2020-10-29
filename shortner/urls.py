from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:prefix>', views.redirect, name='redirect'),
    path('create_link/', views.create_link, name='create')
]
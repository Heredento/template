from tempfile import template
from django.contrib import admin
from django.urls import path
from . import views 
from django.views.generic.base import TemplateView

urlpatterns = [
    # path('', views.index),
    # path('login/', views.login),
    # path('eventos/', views.eventos)
    
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact)
    
]

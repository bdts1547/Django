from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('dn/', views.Login.as_view(), name='login'),



]
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('user_view/', views.UserView.as_view(), name='user_view'),
    path('product_view/', views.product_view, name='product_view'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),


]
from django.urls import path
from . import views



app_name = 'news'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('save/', views.SaveNewsClass.as_view(), name='save'),
    path('email/', views.email_view, name='email'),
    path('sent/', views.email_sent, name='sent'),
]
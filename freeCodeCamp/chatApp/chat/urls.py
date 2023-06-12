from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<str:room>/', views.RoomView.as_view(), name='room'),
    path('checkview', views.Check.as_view(), name='check'),
    path('send', views.Send.as_view(), name='send'),
    path('getMessages/<str:room>/', views.GetMessages.as_view(), name='getMessage'),


]
from django.urls import path
from . import views


urlpatterns = [
    path("", views.Home.as_view(), name='home'),
    path("<str:room>/", views.RoomChat.as_view(), name='room'),
    path("checkroom", views.CheckRoom.as_view(), name='checkroom'),
    path("send", views.Send.as_view(), name='send'),
    path("getMessages/<str:room>/", views.GetMessage.as_view(), name='getMessage'),

]
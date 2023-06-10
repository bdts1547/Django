from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post/<str:pk>', views.PostView.as_view(), name='post'),

]
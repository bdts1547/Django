from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('delete/<str:id>', views.Delete.as_view(), name='delete'),

]
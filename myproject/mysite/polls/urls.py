from django.urls import path
from . import views


urlpatterns = [
    path('detail_view/<int:question_id>', views.detail_view, name='detail'),
    path('list/', views.list_question, name='list_question'),
    path('', views.index, name='index'),
    path('vote/<int:question_id>', views.vote, name='vote'),
]
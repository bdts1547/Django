from django.urls import path
from .views import Index, FileView


urlpatterns = [
    path("upload/", FileView.as_view(), name='upload'),
    path("", Index.as_view(), name='index'),
]
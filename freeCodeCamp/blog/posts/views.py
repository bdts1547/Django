from django.shortcuts import render
from django.views import View
from .models import Post

# Create your views here.
class Index(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'index.html', {'posts': posts})
    

class PostView(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)

        return render(request, 'posts.html', {'post': post})
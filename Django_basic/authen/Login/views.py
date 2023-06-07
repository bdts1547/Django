from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm

# Create your views here.
class Index(View):
    def get(self, request):
        return HttpResponse("Hello")


class Login(View):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'login/success.html')
        else:
            return HttpResponse("Not Exists")


class UserView(LoginRequiredMixin, View):
    login_url="/login/"
    def get(self, request):
        return HttpResponse("View User")    
      


@decorators.login_required(login_url="/login/")
def product_view(request):
    return HttpResponse("Success")


class AddPost(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        postForm = PostForm()
        context = {'postForm': postForm}
        return render(request, 'login/add_post.html', context)

    def post(self, request):
        data = PostForm(request.POST)
        if data.is_valid():
            if request.user.has_perm('login.add_post'):
                data.save()
                return HttpResponse(data)
            else:
                return HttpResponse("Not allowed")
        else:
            return HttpResponse("Invalid data")

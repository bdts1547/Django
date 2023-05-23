from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate



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
            return HttpResponse(username)
        else:
            return HttpResponse("Not Exists")



from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import User


# Create your views here.
class Index(View):
    def get(self, request):
        
        return render(request, 'index.html')
    

class Create(View):
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        description = request.POST['description']
        print(username)
        new_user = User.objects.create(username=username, email=email, desc=description)
        new_user.save()

        return HttpResponse("Add {} successful".format(username))





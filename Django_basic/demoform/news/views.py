from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View




# Create your views here.

class IndexClass(View):
    def get(self, request):
        return HttpResponse("Hi")


class SaveNewsClass(View):
    def get(self, request):
        postForm = PostForm()
        return render(request, 'news/add_news.html', {'postForm': postForm})


    def post(self, request):
        data = PostForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse("Saved")
        else:
            return HttpResponse("Invalid")



def email_view(request):
    sendEmail = SendEmail()
    
    return render(request, 'news/email.html', {'email': sendEmail})


def email_sent(request):
    if request.method == "POST":
        data = SendEmail(request.POST)
        if data.is_valid():
            title = data.cleaned_data['title']
            content = data.cleaned_data['content']
            email = data.cleaned_data['email']
            cc = data.cleaned_data['cc']
            content = {
                'title': title,
                'content': content,
                'email': email,
                'cc': cc
            }
            return render(request, 'news/email_sent.html', content)
        else:
            return HttpResponse("Invalid")
    else:
        return HttpResponse("Not POST")
        

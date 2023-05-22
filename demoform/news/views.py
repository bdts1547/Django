from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
# Create your views here.

def index(request):
    return HttpResponse("Hi")


def add_post(request):
    postForm = PostForm()
    # return HttpResponse("123")
    return render(request, 'news/add_news.html', {'postForm': postForm})



def save_news(request):
    if request.method == "POST":
        data = PostForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse("Saved")
        else:
            return HttpResponse("Invalid")
    else:
        return HttpResponse("Not POST")


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
        

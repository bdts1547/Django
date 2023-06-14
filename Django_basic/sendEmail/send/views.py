from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail


# Create your views here.
class Index(View):
    def get(self, request):
        print(0)
        send_mail(
            "Subject",
            "Message.",
            "bdts1547@gmail.com",
            ["nguyendang1547@gmail.com", "cehoba8402@aramask.com"],
            fail_silently=False)
        print(1)
        return render(request, 'home.html')
from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from .models import File

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
    


class FileView(View):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        list_file = []
        upload_files = request.FILES.getlist('files')
        for file in upload_files:
            new_file = File(file=file)
            new_file.save()
            list_file.append(new_file)
        print(list_file[0].file.url)
        # return render(request, 'upload.html', {'files': [str(x.file.url) for x in list_file]})
        return render(request, 'upload.html', {'file': str(list_file[0].file.url)})


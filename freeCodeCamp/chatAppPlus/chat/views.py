from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Message, Room

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'chat/home.html')
    

class RoomChat(View):
    def get(self, request, room):
        username = request.GET.get('username')
        room_detail = Room.objects.get(name=room)
        return render(request, 'chat/room.html', {
            'username': username,
            'room': room,
            'room_detail': room_detail
        })
    

class CheckRoom(View):
    def post(self, request):
        room_name = request.POST['room_name']
        username = request.POST['username']
        if Room.objects.filter(name=room_name).exists():
            return redirect('/{}/?username={}'.format(room_name, username))
        else:
            new_room = Room.objects.create(name=room_name)
            new_room.save()
            return redirect('/{}/?username={}'.format(room_name, username))
        

class Send(View):
    def post(self, request):
        username = request.POST['username']
        room_id = request.POST['room_id']
        message = request.POST['message']

        new_message = Message.objects.create(username=username, text=message, room_id=Room(id=room_id))
        new_message.save()

        return HttpResponse('Success')
    

class GetMessage(View):
    def get(self, request, room):
        room_detail = Room.objects.get(name=room)
        messages = Message.objects.filter(room_id=room_detail.id)

        return JsonResponse({'messages': list(messages.values())})


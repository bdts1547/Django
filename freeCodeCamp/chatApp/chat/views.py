from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html')
    

class RoomView(View):
    def get(self, request, room):
        username = request.GET.get('username')
        room_detail = Room.objects.get(name=room)

        return render(request, 'room.html', {
            "username": username,
            'room': room,
            'room_detail': room_detail
        })
    
class Check(View):
    def post(self, request):
        room = request.POST['room_name']
        username = request.POST['username']
        if Room.objects.filter(name=room).exists():
            return redirect('/{}/?username={}'.format(room, username))
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect('/{}/?username={}'.format(room, username))
        

class Send(View):
    def post(self, request):
        username = request.POST['username']
        message = request.POST['message']
        room_id = request.POST['room_id']

        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()

        return HttpResponse("hi")
    

class GetMessages(View):
    def get(self, request, room):
        room_detail = Room.objects.get(name=room)
        messages = Message.objects.filter(room=room_detail.id)
        
        print(list(messages.values()))
        return JsonResponse({'messages': list(messages.values())})










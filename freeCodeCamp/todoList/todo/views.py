from django.shortcuts import render, redirect
from django.views import View
from .models import Todo

# Create your views here.
class Index(View):
    def get(self, request):
        todoList = Todo.objects.all()


        return render(request, 'index.html', {'todos': todoList})
    

    def post(self, request):
        title = request.POST['title']
        new_todo = Todo(title=title)
        new_todo.save()

        return redirect('/')


class Delete(View):
    def get(self, request, id):
        obj_delete = Todo.objects.get(id=id)
        obj_delete.delete()

        return redirect('/')
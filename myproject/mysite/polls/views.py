from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.

def index(request):
    my_name = "dang nguyen"
    context = {"name": my_name}
    return render(request, "polls/index.html", context)


def list_question(request):
    list_question = Question.objects.all()
    # list_question = get_object_or_404(Question, pk=1)

    context = {"listQ": list_question}
    return render(request, "polls/question_list.html", context) 


def detail_view(request, question_id):
    q = Question.objects.get(pk=question_id)
    context = {'q': q}
    
    return render(request, "polls/detail_question.html", context)


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST['choice']
        c = q.choice_set.get(pk=data)
        c.vote += 1
        c.save()
    except:
        HttpResponse("Error no data")
    context = {'q': q}
    return render(request, 'polls/result.html', context)

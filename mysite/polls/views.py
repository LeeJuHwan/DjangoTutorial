from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


def index(request):
    ctx = {
        "greetings" : "Hello there!",
        "location" : {
            "city" : "seoul",
            "country" : "South Korea"
        },
        "languages" : ["Korean", "English"]
    }
    return render(request, "polls/main.html", context=ctx)

def detail(request, question_id) :
    return HttpResponse(f"looking at question_id page {question_id}.")

def results(request, question_id) :
    response = "Yoe're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id) :
    return HttpResponse(f"looking at voting at question page {question_id}.")
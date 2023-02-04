from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from polls.models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by("pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list" : latest_question_list
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list" : latest_question_list}
    return render(request, "polls/index.html", context)



def detail(request, question_id) :
    return HttpResponse(f"looking at question_id page {question_id}.")

def results(request, question_id) :
    response = "Yoe're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id) :
    return HttpResponse(f"looking at voting at question page {question_id}.")
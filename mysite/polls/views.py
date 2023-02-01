from django.http import HttpResponse


def index(request):
    return HttpResponse("polls index")

def detail(request, question_id) :
    return HttpResponse(f"looking at question_id page {question_id}.")

def results(request, question_id) :
    response = "Yoe're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id) :
    return HttpResponse(f"looking at voting at question page {question_id}.")
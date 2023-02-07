from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from polls.models import Question, Choice, Survey
from django.http import Http404
from polls.forms import SurveyForm


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
    try :
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("해당 질문을 찾을 수 없습니다.")
    return render(request, "polls/detail.html", {"question" : question})

def results(request, question_id) :
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/results.html", {"question" : question})

def vote(request, question_id) :
    question = get_object_or_404(Question, pk = question_id)
    print(question)
    try :
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {"question" : question, "error_message" : "항목을 선택하지 않았습니다."})

    else :
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args = (question_id,)))


def survey(request):
  
    if request.method == 'POST':
    
        form = SurveyForm(request.POST)
        if form.is_valid():

            #update
            # survey = Survey.objects.get(pk = 1)
            # form = SurveyForm(request.POST, instance = survey)
            form.save()
            return HttpResponseRedirect(reverse("polls:thanks"))
    else:
        form = SurveyForm()

    return render(request, "polls/survey_custom.html", {"form" : form})

def thanks(request) :
    return render(request, "polls/thanks.html", {})

    
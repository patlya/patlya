from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." ,  question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    latest_question_list = Question.objects.all() #order_by('-pub_date')[:5]
    # render.....
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



    # loader ....
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

# def detail(request):
#     try:
#         question = Question.objects.get(pk=4)
#         import pip
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

    
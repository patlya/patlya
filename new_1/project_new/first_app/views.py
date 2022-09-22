#from django.shortcuts import render

# Create your views here.

#user-name=ranu
#password=ranu123

from django.http import HttpResponse

# def show(request):
#     return HttpResponse("today's we create new project and do a lot of practice ")

# def student(request,student_id):
#     return HttpResponse("heloo my id is ...",student_id) 





#from django.template import loader

from .models import Question

# def index(request):
#     all_ques=Question.objects.all()
#     for a in all_ques:
#         url='/student/'+str(a.student_id)+'/'
#         x='<a href=" '+url+' ">'+a.question_text +'</a><br>'
#         return HttpResponse(x)



# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('first_app/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

from django.http import Http404
from django.shortcuts import render

#from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
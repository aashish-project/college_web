from django.shortcuts import render,HttpResponse ,redirect,get_object_or_404
from .models import*
import random
# Create your views here.
from django.http import HttpResponseNotFound,JsonResponse

def favicon(request):
    return HttpResponseNotFound()

def temp(request):
    if request.method == 'POST':
        selected_options = request.POST.getlist('my_select')
        print(selected_options)
        return HttpResponse(selected_options)
    return render(request,"fashion.html")

def display_data(request,branch_slug=None,subject_slug=None,chapter_slug=None):
    branches = Branch.objects.all()
    subjects = Subject.objects.all()
    chapters = Chapter.objects.all()
    context = {'branches': branches, 'subjects': subjects, 'chapters': chapters}
    if subject_slug:
        branch = get_object_or_404(Branch, branch=branch_slug)
        subject = get_object_or_404(Subject, branch=branch, subject=subject_slug)
        chapters = subject.chapter_set.all()
        context.update({'chapters':chapters})
    if chapter_slug:
        chapter=get_object_or_404(Chapter,chapter=chapter_slug)
        topic=chapter.topic_set.all()
        context.update({'topics':topic})
        pass
    # print(context)
    return render(request, 'home.html', context)

def question_list(request):
    if request.method =='POST':
        selected_topics=request.POST.getlist('my_select')
        questions=check_question(request,selected_topics)
        random.shuffle(questions)
        context={'questions':questions}
    return render(request,'question_list.html',context)


def check_question(request,topics)->list:
    questions=[]
    for topic in topics:
        topic_obj=Topic.objects.get(topic=topic)
        questions.append(Question.objects.filter(topic__topic__iexact=topic).order_by('?'))
    return questions
from django.shortcuts import render
from .models import Work, Complete, HappyCustomer, Skill


def index_view(request):
    works = Work.objects.all()
    completed = Complete.objects.all()[0:4]
    happy_customers = HappyCustomer.objects.all()
    skills = Skill.objects.all()
    return render(request, 'index.html',
                  {'works': works,
                   'completed': completed,
                   'happy_customers': happy_customers,
                   'skills': skills
                   })


def my_works_view(request):
    works = Work.objects.all()
    return render(request, 'my_works.html', {'works': works})


def hire_me_view(request):
    return render(request, 'hire_me.html')


def about_view(request):
    return render(request, 'about.html')


def web_development_view(request):
    return render(request, 'web_development.html')


def web_design_view(request):
    return render(request, 'web_design.html')


def python_programming_view(request):
    return render(request, 'python_programming.html')

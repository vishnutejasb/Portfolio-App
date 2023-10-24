from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from projects.models import Project

def testing(request):
    #1st return HttpResponse("hello world")
    #myprojects=Project.objects.all().values()
    template=loader.get_template('about_me.html')
    '''context={
        'myprojects':myprojects
    }'''
    return HttpResponse(template.render())

def project_index(request):
    projects = Project.objects.all()
    template=loader.get_template('project_index.html')
    context = {
        "projects": projects
    }
    return HttpResponse(template.render(context,request))

def project_detail(request, pk):
    myprojects = Project.objects.get(pk=pk)
    template=loader.get_template('project_detail.html')
    context = {
        "myprojects": myprojects
    }
    return HttpResponse(template.render(context,request))


# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def projects(request):
    projects = models.Project.objects.all() # quering all the projects and storing in projects
    context = {'projects': projects}
    return render(request, 'application/projects.html', context)

def project(request, pk):
    projectObj = models.Project.objects.get(id=pk) # single project should match with it's id.
    context = {
        'project': projectObj
    }
    return render(request, 'application/single__project.html', context)

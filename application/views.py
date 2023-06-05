from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms


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

def createProject(request):
    form = forms.ProjectForm()  # takes ProjectForm class from forms.py and store as form
    context = {
        'form': form    # form will be used in templates to create a form.
    }
    return render(request, 'application/project__form.html', context)

from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import forms
from django.db.models import Q 
# from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

# Create your views here.
def projects(request):  # list view
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = models.Tag.objects.filter(name__icontains = search_query)
    projects = models.Project.objects.distinct().filter(Q(title__icontains = search_query) | 
    Q(description__icontains = search_query) |
    Q(owner__name__icontains = search_query) |
    Q(tags__in = tags)) # quering all the projects by it's title or tagname and storing in projects
    
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(projects, results)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
    
    context = {'projects': projects, 'search_query' : search_query, 'paginator': paginator}
    return render(request, 'application/projects.html', context)

def project(request, pk):   # detail view
    projectObj = models.Project.objects.get(id=pk) # retrieve single project object from the db using it's pk.
    form = forms.ReviewForm()

    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        projectObj.getVoteCount
        return redirect('project', pk = projectObj.id)

    context = {
        'project': projectObj,
        'form': form
    }
    return render(request, 'application/single__project.html', context)

@login_required(login_url="login")
def createProject(request):     # create view
    profile = request.user.profile
    form = forms.ProjectForm()  # takes ProjectForm class from forms.py and store as form
    if request.method == 'POST':    # first checks whether the request is POST or not.
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = forms.ProjectForm(request.POST, request.FILES)  # when the request is POST take the form to accept POST request.  
        # with request.FILES user will be able to add files in POST request.
        if form.is_valid():     # checks if the form is valid
            project = form.save(commit=False)
            project.owner = profile
            project.save() # save the instance to the database if the form is valid.
            for tag in newtags:
                tag, created = models.Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account') # redirect to projects url after saving the form.
    context = {
        'form': form    # form will be used in templates to create a form.
    }
    return render(request, 'application/project__form.html', context)

@login_required(login_url="login")
def updateProject(request, pk): # update view
    profile = request.user.profile # getting the profile of logged in user
    project = profile.project_set.get(pk=pk) # retrieve the single project object of that logged in user from the db using it's pk.
    form = forms.ProjectForm(instance = project) # form will be pre-populated with the existing data from that object.
    if request.method == 'POST':    # if the method is 
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = forms.ProjectForm(request.POST, request.FILES, instance = project) # with POST request prepopulate the data.
        if form.is_valid:
            project = form.save()
            for tag in newtags:
                tag, created = models.Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    context = {'form': form, 'project': project}
    return render(request, 'application/project__form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk): # delete view
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
    if request.method == 'POST':
        project.delete()    # deletes the project from the database.
        return redirect('account')
    context = {'object': project}   # project is defined as object variable which can be used to identify the project in confirm__delete
    return render(request, 'application/confirm__delete.html', context)


# CRUD OPERATION With Generic Views, we can directly create forms without creating forms.py with generic views.

# Create View

# class CreateProject(CreateView):    # CreateView parameter will allow the user to create a new object
#     model = models.Project          # takes the Project model fields to create a form.
#     template_name = 'application/project__form.html'    # head over to this template after CreateProject class is invoked.
#     fields = ['title', 'description', 'demo_link', 'source_link', 'tags']   # only take these views.
#     success_url = 'projects'        # after succesfully submission of form head over to this url.

# List View

# class ListProject(ListView):
#     model = models.Project
#     template_name = 'application/projects.html' # head over to this template to view list of all the projects
#     context_object_name = 'projects'    # name of object as projects

# Detail View

# class DetailProject(DetailView):
#     model = models.Project
#     template_name = 'application/single__project.html'  # head over to this template to view the project in detail.
     

# Update View

# class UpdateProject(UpdateView):
#     model = models.Project
#     template_name = 'application/project__form.html'
#     fields = ['title', 'description', 'demo_link', 'source_link', 'tags']
#     success_url = '/projects'

# Delete View

# class DeleteProject(DeleteView):
#     template_name = 'application/confirm__delete.html'
#     success_url = '/projects'

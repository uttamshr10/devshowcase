from django.shortcuts import render, redirect
from django.contrib import messages
from users import models
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def registerPage(request):
    page = 'register'
    form = CustomUserCreationForm()   # default form of django
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # saving the instance of form.
            user.username = user.username.lower() # lowercasing the username.
            user.save() # save the user detail.

            messages.success(request, "Successfully registered.") # show success flash message
            login(request, user)
            return redirect('edit-account') # after successfully registered head over to edit account. 
        
        else:
            messages.error(request, "User cannot be registered.")


    context={
        'page' : page,
        'form': form,
    }

    return render(request, 'users/loginandregister.html', context)

def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == "POST":    # when request method is POST
        username = request.POST['username'].lower() # store the username sent as a POST method.
        password = request.POST['password'] # store the passord sent as a POST method.
        try:
            user = User.objects.get(username=username)  # first level authentication, checking username.
        except:
            messages.error(request, "Username doesn't exist.")    # execute if the username doesn't exist.
        
        user = authenticate(request, username = username, password = password) # check whether the username and password matches with the username and password provided.
        if user:
            login(request, user) # to add session to the browser's cookie.
            return redirect(
                request.GET['next'] if 'next' in request.GET else 'account'  
            ) # if the credentials are correct, redirect to account.
        else:
            messages.error(request, "Credential incorrect.")  # if the credentials are incorrect, either one or both.
    return render(request, 'users/loginandregister.html')

def logoutPage(request):
    logout(request)
    messages.info(request, "Logout successfully.") # shows logged out message when user is logged out.
    return redirect("login")

def Profile(request):   
    search_query = '' # set the search query to empty string
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query') # get the search query and store inside search query
    
    skills = models.Skill.objects.filter(name__icontains = search_query)
    profiles = models.Profile.objects.distinct().filter(Q(name__icontains=search_query) | 
    Q(short_intro__icontains = search_query) | 
    Q(skill__in=skills)) # filter the profile which contains name, title and skills and store in profiles.
    
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(profiles, results)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
    
    
    context = {'profiles': profiles, 'search_query': search_query, 'paginator': paginator}    # set profiles [key] and profiles [value] to use in template later.
    return render(request, 'users/profiles.html', context)  # pass context to use those variables in template.


def userProfile(request, pk):
    profile = models.Profile.objects.get(id=pk) # get the objects matched by its id.
    # exclude all the skills if it's description is null to place it in other skills.
    topSkills = profile.skill_set.exclude(description__exact="") # exclude skills that doesn't have description
    # include skills that has empty description to store in other skills as well. 
    otherSkills = profile.skill_set.filter(description="") # give value of empty description
    context = {
        'profile': profile,
        'topSkills': topSkills,
        'otherSkills': otherSkills
    }
    return render(request, 'users/user-profile.html', context)

@login_required(login_url = 'login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance = profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form': form
    }
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            return redirect('account')

    context = {
        'form': form
    }
    return render(request, 'users/skill_form.html', context)

@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(pk=pk)
    form = SkillForm(instance = skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {
        'form': form
    }
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(pk=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('account')
    context = {
        'object': skill
    }
    return render(request, 'application/confirm__delete.html', context)


@login_required(login_url = 'login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {
        'messageRequests' : messageRequests,
        'unreadCount' : unreadCount
    }
    return render(request, 'users/inbox.html', context)

@login_required(login_url = 'login')
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(pk=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message': message}
    return render(request, 'users/message.html', context)

def sendMessage(request, pk):
    recipient = models.Profile.objects.get(id=pk)
    form = MessageForm
    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()
            return redirect('user-profile', pk = recipient.id)
    
    context = {
        'form' : form,
        'recipient' : recipient
    }
    return render(request, 'users/message_form.html', context)
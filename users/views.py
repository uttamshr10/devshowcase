from django.shortcuts import render, redirect
from django.contrib import messages
from users import models
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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
            return redirect('edit-account') # after successfully registered head over to user profiles. 
        
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
        username = request.POST['username'] # store the username sent as a POST method.
        password = request.POST['password'] # store the passord sent as a POST method.
        try:
            user = User.objects.get(username=username)  # first level authentication, checking username.
        except:
            messages.error(request, "Username doesn't exist.")    # execute if the username doesn't exist.
        
        user = authenticate(request, username = username, password = password) # check whether the username and password matches with the username and password provided.
        if user:
            login(request, user) # to add session to the browser's cookie.
            return redirect("profiles") # if the credentials are correct, redirect to profiles.
        else:
            messages.error(request, "Credential incorrect.")  # if the credentials are incorrect, either one or both.

    return render(request, 'users/loginandregister.html')

def logoutPage(request):
    logout(request)
    messages.info(request, "Logout successfully.") # shows logged out message when user is logged out.
    return redirect("login")

def Profile(request):   
    profiles = models.Profile.objects.all() # query all the profiles and store in profiles.
    context = {'profiles': profiles}    # set profiles [key] and profiles [value] to use in template later.
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

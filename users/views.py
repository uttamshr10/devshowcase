from django.shortcuts import render, redirect
from users import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == "POST":    # when request method is POST
        username = request.POST['username'] # store the username sent as a POST method.
        password = request.POST['password'] # store the passord sent as a POST method.
        try:
            user = User.objects.get(username=username)  # first level authentication, checking username.
        except:
            print("Username doesn't exist.")    # execute if the username doesn't exist.
        
        user = authenticate(request, username = username, password = password) # check whether the username and password matches with the username and password provided.
        if user:
            login(request, user) # to add session to the browser's cookie.
            return redirect("profiles") # if the credentials are correct, redirect to profiles.
        else:
            print("Credential incorrect.")  # if the credentials are incorrect, either one or both.

    return render(request, 'users/register.html')

def logoutPage(request):
    logout(request)
    return redirect("register")

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

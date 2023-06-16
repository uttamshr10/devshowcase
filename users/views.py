from django.shortcuts import render
from users import models

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

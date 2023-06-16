from django.shortcuts import render
from users import models

def Profile(request):   
    profiles = models.Profile.objects.all() # query all the profiles and store in profiles.
    context = {'profiles': profiles}    # set profiles as profiles to use in template later.
    return render(request, 'users/profiles.html', context)  # pass context to use those variables in template.

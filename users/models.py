from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete # for django signals.
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)  # User has one to one relationship with their Profile means user can create only one Profile.
    name = models.CharField(max_length = 100, blank = True, null = True)
    email = models.EmailField(max_length = 50, blank = True, null = True)
    username = models.CharField(max_length = 20, blank = True, null = True)
    short_intro = models.CharField(max_length = 200, blank = True, null = True)
    location = models.CharField(max_length = 200, blank = True, null = True)
    bio = models.TextField(blank = True, null = True)
    profile_image = models.ImageField(null = True, blank = True, upload_to = 'users/', default='users/user-default.png')
    # uploaded image should upload to users folder of images folder in static folder, if no image is uploaded give default image.
    social_github = models.CharField(max_length = 200, blank = True, null = True)     # user can add github
    social_linkedin = models.CharField(max_length = 200, blank = True, null = True)   # user can add linkedin
    social_website = models.CharField(max_length = 200, blank = True, null = True)    # user can add their website.
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)


    def __str__(self):
        return str(self.user.username)
    

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank = True, null = True) # when Profile is deleted, delete skill too.
    name = models.CharField(null = True, blank = True, max_length = 40) # name of the skill that user has
    description = models.TextField(null = True, blank= True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)

    def __str__(self):
        return self.name

@receiver(post_save, sender=Profile) # this is similar to post_save.connect()
def updatedProfile(sender, instance, created, **kwargs):
    print("Profile updated.")
    print("Instance: ", instance)   # prints instance of the profile.
    print("Sender: ", sender) # prints object of sender i.e users.models.Profile
    print("Created: ", created) # prints True if new profile is created else print False

@receiver(post_delete, sender=Profile)
def deleteProfile(sender, instance, **kwargs):
    print("Deleting...")
    print("Instance", instance) # prints user i.e instance in console.

# post_save.connect(updatedProfile, sender=Profile) # trigger updateProfile when sender -> Profile model is called. 

# post_delete.connect(deleteProfile, sender=Profile) # trigger deleteProfile when Profile model is deleted.

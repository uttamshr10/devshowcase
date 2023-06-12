from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)  # User has one to one relationship with their Profile means user can create only one Profile.
    name = models.CharField(max_length = 100, blank = True, null = True)
    email = models.EmailField(max_length = 50, blank = True, null = True)
    username = models.CharField(max_length = 20, blank = True, null = True)
    short_intro = models.CharField(max_length = 200, blank = True, null = True)
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

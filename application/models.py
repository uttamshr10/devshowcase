from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Project (models.Model):
    owner = models.ForeignKey(Profile, blank = True, null = True, on_delete = models.SET_NULL )  # Create the owner for the project and don't delete the project when the user id is deleted by any circumstances.
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True, null = True)
    project_image = models.ImageField(blank = True, null = True, default = "default.jpg") # to add images to the DB.
    demo_link = models.CharField(max_length=2000, blank = True, null = True)
    source_link = models.CharField(max_length = 2000, blank = True, null = True)
    tags = models.ManyToManyField('Tag', blank = True)  # it lets user select content of Tag table.
    vote_total = models.IntegerField(default = 0, null = True, blank = True)
    vote_ratio = models.IntegerField(default = 0, null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False) # generate random unique id

    def __str__(self):
        return self.title

class Review(models.Model):
    # let the user vote
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    project = models.ForeignKey('Project', on_delete=models.CASCADE) # user can select the project which they want to review
    body = models.TextField(blank=True, null = True)
    value = models.CharField(max_length = 20, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False) # generate a random UUID as the default value.
    # UUID are used to identify records in a database.

    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False) # generate random unique ID 

    def __str__(self):
        return self.name


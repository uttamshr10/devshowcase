from django.db import models
import uuid

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True, null = True)
    demo_link = models.CharField(max_length=2000, blank = True, null = True)
    source_link = models.CharField(max_length = 2000, blank = True, null = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.title

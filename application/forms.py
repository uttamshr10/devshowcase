from django.forms import ModelForm
from . import models

class ProjectForm(ModelForm):   # model form that creates the form out of model.
    class Meta:                 # meta class takes two parameters model and fields.
        model = models.Project  # create a form out of Project model
        fields = ['title', 'project_image', 'description', 'demo_link', 'source_link', 'tags']      # selecting all the fields

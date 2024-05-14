from django.forms import ModelForm
from . import models
from django import forms

class ProjectForm(ModelForm):   # model form that creates the form out of model.
    class Meta:                 # meta class takes two parameters model and fields.
        model = models.Project  # create a form out of Project model
        fields = ['title', 'project_image', 'description', 'demo_link', 'source_link', 'tags']      # selecting all the fields
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),  # making the tags field a checkbox to select multiple options
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # to change the attribute of every form field.
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})   # with this we can loop and give class to multiple form fields.

class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }
        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


        # to change the attribute of the field, any HTML attribute.
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Your title here.'})
        # self.fields['description'].widget.attrs.update({'class': 'input'})
        # self.fields['demo_link'].widget.attrs.update({'class': 'input'})
        # self.fields['source_link'].widget.attrs.update({'class': 'input'})

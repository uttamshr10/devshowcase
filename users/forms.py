from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']  # in a form only show first name, email username and password with confirmation while filling.
        labels = {
            'first_name': 'Name',       # changing the label from first name to Name to ensure the user will type full name instead of first name only.
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # to change the attribute of every form field.
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})   # with this we can loop and give class to multiple form fields.

class ProfileForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ['name', 'email', 'username', 'short_intro', 'location', 'bio', 'profile_image', 'social_github', 'social_linkedin', 'social_website']


    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class SkillForm(ModelForm):
    class Meta:
        model = models.Skill
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
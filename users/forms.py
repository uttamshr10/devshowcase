from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']  # in a form only show first name, email username and password with confirmation while filling.
        labels = {
            'first_name': 'Name',       # changing the label from first name to Name to ensure the user will type full name instead of first name only.
        }

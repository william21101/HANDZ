from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    """
    This class extends the UserCreationForm, adding in extra fields for first
    name, last name, and email.
    """
    first_name = forms.CharField(max_length=30,
                                 required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30,
                                required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254,
                             help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )

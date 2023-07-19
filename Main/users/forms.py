from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import Profile

# Create your forms here.


# A form extended from UserCreationForm for our custom user Profile
class ProfileCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Profile
        fields = UserCreationForm.Meta.fields + ('university', 'first_name',
                                                 'last_name','user_type')
        help_texts = {
            'username': None,
        }

    

# A form for changing user details, but has not been used yet
class ProfileChangeForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = UserChangeForm.Meta.fields

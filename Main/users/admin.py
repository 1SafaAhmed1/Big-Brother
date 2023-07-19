from django.contrib import admin
from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile

# Register your models here.

admin.site.register(Profile)

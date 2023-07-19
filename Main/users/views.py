from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse

from .models import Profile
from .forms import ProfileCreationForm

# Create your views here.


# Registration view that renders registration.html with a ProfileCreationForm
class RegistrationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('register_success') 


# A success view that renders a html page with success message
def register_success_view(request):

   return render(request, 'account/register_success.html', {})
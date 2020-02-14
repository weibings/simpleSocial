from django.shortcuts import render, redirect
from . import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lay
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
class SignUpView(CreatView):
    model = forms.SignUpForm
    success_url = reverse_lay('login')
    template_name = 'account/signup.html'

def login_request(request):
    form = AuthenticationForm()
    return render(request, template_name='accounts/login.html', name='login')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")

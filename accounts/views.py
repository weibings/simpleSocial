from django.shortcuts import render, redirect
from . import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
class SignUpView(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    # fields = '__all__'

def login_request(request):
    form = AuthenticationForm()
    return render(request, template_name='accounts/login.html', context={'form':form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")

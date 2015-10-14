from django.shortcuts import render
from django.contrib.auth import login
# Create your views here.
from .forms import UserCreationEmailForm, EmailAuthenticateForm

def signup(request):
    form = UserCreationEmailForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    form = EmailAuthenticateForm(request.POST or None)

    if form.is_valid():
        login(request, form.get_user())

    return render(request, 'signin.html', {'form':form})
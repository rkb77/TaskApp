from django.shortcuts import render, redirect
from django.http import HttpResponse
from users_App.forms import CustomRegisterForm
from django.contrib import messages

def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New user account Created!, Login to Get Started"))
            return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

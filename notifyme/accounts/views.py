from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account successfully created!")
            return redirect("login")
        
    else:
        form = UserCreationForm()

    return render(request, 'register.html', context={"form":form})

def profile(request):
    return render(request, 'profile.html')
    
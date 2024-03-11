from django.shortcuts import render, redirect
from .forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/auth/login")
    else:
        form = SignupForm()
    return render(request, "authentication/signup.html", {"form":form})
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import auth
from genotip.forms import LoginForm

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            return redirect("index")
    
    login_form = LoginForm()
    
    context = {"login_form": login_form}

    return render(request, "genotip/login.html", context)
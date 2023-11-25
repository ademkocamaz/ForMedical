from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import auth
from genotip.forms import LoginForm
from django.contrib import messages

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        service = request.POST["service"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session.set_expiry(300)
            request.session["service"] = service
            return redirect("index")
        else:
            messages.add_message(request, messages.ERROR, 'Kullanıcı Adı veya Parola hatalı. Giriş Bilgilerini kontrol ediniz.')

    login_form = LoginForm()

    context = {"login_form": login_form}

    return render(request, "genotip/login.html", context)

def logout(request):
    auth.logout(request)
    return redirect("index")
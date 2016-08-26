from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def show_login(request):
    if request.method == "GET":
        return render(request, "dust_auth/login.html")
    else:
        context = make_login(request)

        if context.get('is_logged'):
            return redirect(reverse("home:index"))
        else:
            return render(request, "dust_auth/login.html", context)

def make_login(request):
    form = request.POST
    username = form.get('username')
    password = form.get('password')

    user = authenticate(username=username, password=password)
    is_logged = False

    if user is not None:
        login(request, user)
        message = "Logged"
        is_logged = True
    else:
        message = "Incorrect user"

    context = {
        "is_logged": is_logged,
        "message": message,
    }

    return context

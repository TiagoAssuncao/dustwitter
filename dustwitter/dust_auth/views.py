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

def signup(request):
    if request.method == "GET":
        return render(request, "dust_auth/signup.html")
    else:
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        email = form.get('email')

        user = User.objects.create_user(username, email, password)
        user.save()

        return redirect(reverse("auth:login"))

def make_logout(request):
    logout(request)
    return redirect(reverse("home:index"))

def users(request):
    users = User.objects.all()

    user_perm = []
    for user in users:
        can_read = 'checked' if user.has_perm('comment.can_read') else ''
        can_comment = 'checked' if user.has_perm('comment.can_comment') else ''
        print(can_read, can_comment)
        user_perm.append({
            "current_user": user,
            "can_read": can_read,
            "can_comment": can_comment,
        })

    context = {"users": user_perm}

    return render(request, "dust_auth/users.html", context)

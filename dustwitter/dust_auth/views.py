from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "dust_auth/login.html")
    else:
        make_login(request)
        return render(request, "dust_auth/login.html")

def make_login(request):
    form = request.POST
    print(form.get('username'))
    print(form.get('password'))

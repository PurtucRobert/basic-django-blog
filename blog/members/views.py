from re import I
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('front_page')
        else:
            messages.success(
                request, ("There was an error logging in, try again.."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == 'POST':
        # User has information and wants to login
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already exists!!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')

        else:
            # User wants to reach the sign up page
            return render(request, 'accounts/signup.html',{'error': 'Password do not match!!'})
    else:
        # User wants to reach the sign up page
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Login credentials invalid'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

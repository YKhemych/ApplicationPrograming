from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confPassword']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                userName = request.POST['username'].split(" ");
                user = User.objects.create_user(request.POST['username'], password = request.POST['password'], first_name = userName[0], last_name = userName[1] )
                auth.login(request, user)
                return redirect('allEvents')
        else:
            return render(request, 'accounts/signup.html', {'error':'Password must match'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'] )
        if user is not None:
            auth.login(request, user)
            return redirect('allEvents')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

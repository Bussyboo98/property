from django.shortcuts import render, redirect


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login.html')

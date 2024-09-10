from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# def login(request):
#     return render(request, 'finance/login.html')

@login_required
def home(request):
    return render(request, 'finance/charitechlogin.html')

@login_required
def about(request):
    return render(request, 'finance/charitechabout.html')

@login_required
def contact(request):
    return render(request, 'finance/charitechcontact.html')

@login_required
def blog(request):
    return render(request, 'finance/charitechblog.html')
@login_required
def course(request):
    return render(request, 'finance/charitechcourse.html')

def login_signup_view(request):
    if request.method == 'POST':
        print(request.POST)
        action = request.POST.get('action')

        email = request.POST.get('email')
        password = request.POST.get('password')

        if action == 'signup':
            username = request.POST.get('username')

            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password =password)
                user.save()
                login(request,user)
                messages.success(request,'Account created successfully! Welcome')
                return redirect('home')
            
            else:
                messages.error(request, 'Username already exists.')
        
        elif action == 'login':
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials.')
            
    return render(request, 'registration/login.html')



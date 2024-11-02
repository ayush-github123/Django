from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST['password']
        repeat_password = request.POST.get('repeatpassword')

        if(password == repeat_password):
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password = password)

        if user is not None:
            auth.login(request,user)
            return render(request,'index.html',{'username':username})
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')        
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')


def books2(request):
    book = ['action','romantic', 'thriller', 'horror', 'murder mystery']
    return render(request, 'book2.html',  {'book':book})

def books(request, genre):
    return render(request, 'book.html',  {'genre':genre})


    

# def about(request):
#     return render(request, 'about.html')

# def projects(request):
#     return render(request, 'projects.html')

# def skills(request):
#     return render(request, 'skills.html')
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        image = request.POST['image']
        post = {'title':title, 'content':content, 'image':image }
        return render(request,  'index.html', post)
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        else:
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password == confirm_password:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Account created successfully')
    return render(request, 'register.html')




def logout(request):
    pass
    


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        author = request.user  # Get the currently logged-in user

        # Create the new post
        post = Post(title=title, content=content, image=image, author=author)
        post.save()

        return redirect('index')  # Redirect to some page after creation
    return render(request, 'createPost.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from login import settings
from django.core.mail import send_mail

def home(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, 'Login Successful')
            return redirect('signedin')  # Redirect to the signed-in page
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')  # Redirect to the login page with error message

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

                # Welcome Email
                subject = 'Welcome to django-login page!'
                message = f'Hello {username}!\nWelcome to django-login. Thank you for logging in. We have also sent you a confirmation email. Kindly confirm your email to ACTIVATE your account.\n\nThank you,\nAyush Rai'
                from_email = settings.EMAIL_HOST_USER
                to_list = [email]

                # Send the email with error handling
                try:
                    send_mail(subject, message, from_email, to_list, fail_silently=False)
                except Exception as e:
                    print(f"Error sending email: {e}")
                    messages.error(request, "There was an issue sending the email.")

                return redirect('signin')  # Redirect to the login page after registration
            else:
                messages.error(request, 'Passwords do not match')
                return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def signout(request):
    logout(request)
    # messages.success(request, "Logged out successfully.")
    return redirect('home')  # Redirect to home or login page

def signedin(request):
    return render(request, 'indexafterLogin.html')

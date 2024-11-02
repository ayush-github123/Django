from django.shortcuts import render, redirect, get_object_or_404
from .models import book, bookmark
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    query = request.GET.get('q')
    books = book.objects.all()

    if query:
        books = book.objects.filter(title__icontains=query)

    no_results = not books.exists() if query else False

    favorites = bookmark.objects.filter(user=request.user).values_list('book_id', flat=True) if request.user.is_authenticated else []

    context = {
        'books': books,
        'favorites': favorites,
        'no_results': no_results,
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def add_fav(request, book_id):
    if request.user.is_authenticated:
        book_instance = get_object_or_404(book, id=book_id)
        bookmark.objects.get_or_create(user=request.user, book=book_instance)
        messages.success(request, f'{book_instance.title} has been added to your favorites.')
    else:
        messages.warning(request, 'You need to log in to add favorites.')
        return redirect('login')
    return redirect('index')

def del_fav(request, book_id):
    if request.user.is_authenticated:
        book_instance = get_object_or_404(book, id=book_id)
        bookmark.objects.filter(user=request.user, book=book_instance).delete()
        messages.success(request, f'{book_instance.title} has been removed from your favorites.')
    return redirect('index')


def favourites(request):
    if request.user.is_authenticated:
        favourites = bookmark.objects.filter(user = request.user).select_related('book')
        return render(request, 'bookmark.html', {'favourites':favourites})
    else:
        return redirect('login')



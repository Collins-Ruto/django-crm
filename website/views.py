import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

logger = logging.getLogger(__name__)

logger.debug("This is a debug messages")


def home(request):  # Create your views here.
    # check if login request
    print("method", request.method)
    logger.info(request.method)

    records = Record.objects.all()

    if request.method == "POST":
        logger.info(request.POST['username'])
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Hello, You are logged in ...")
            return redirect("home")

        messages.success(request, "Sorry, Invalid credentials, try again ...")
        return redirect("home")

    return render(request, "home.html", {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out ...")
    return redirect("home")

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Hello, You are logged in")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})

def customer_record(request, p_k):
    if request.user.is_authenticated:
        record = Record.objects.get(id=p_k)
        return render(request, 'record.html', {'record': record})

    messages.success(request, "Sorry, You need to be logged in ...")
    return redirect('home')

def delete_record(request, p_k):
    if request.user.is_authenticated:
        record = Record.objects.get(id=p_k)
        record.delete()
        messages.success(request, "Record deleted successfully ...")
        return redirect('home')

    messages.success(request, "You need to be logged in ...")
    return redirect('home')

def add_record(request):
    return render(request, 'add_record.html', {})
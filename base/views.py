from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Event, Type
from .forms import EventForm


def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username Or Password was not correct")

    context = {"page":page}
    return render(request, "base/login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect("home")

def registerPage(request):    
    form = UserCreationForm()

    if request.method == "POST":
        print(request)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occurred during registration")

    return render(request, "base/login_register.html", {"form":form})

def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    events = Event.objects.filter(
        Q(type__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    types = Type.objects.all()
    events_count = events.count()
    context = {
        "events":events,
        "events_count": events_count,
        "types": types
        }
    return render(request, "base/home.html", context)

def event(request, pk):
    event = Event.objects.get(id=pk)
    context = {"event":event}
    return render(request, "base/event.html", context)

@login_required(login_url="login")
def createEvent(request):
    form = EventForm
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/event_form.html", context)

@login_required(login_url="login")
def updateEvent(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)

    if request.user != event.host:
        return HttpResponse("You are not the owner!")

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/event_form.html", context)

@login_required(login_url="login")
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj":event})


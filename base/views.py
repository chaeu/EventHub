from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Event, Type
from .forms import EventForm


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
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

    context = {}
    return render(request, "base/login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect("home")

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

def createEvent(request):
    form = EventForm
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/event_form.html", context)

def updateEvent(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/event_form.html", context)

def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj":event})


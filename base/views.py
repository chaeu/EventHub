from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def home(request):
    events = Event.objects.all()
    context = {"events":events}
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
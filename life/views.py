from django.shortcuts import render, get_object_or_404, redirect

from .models import Person, Event
from .forms import PersonForm, EventForm


def person_list(request):
    persons = Person.objects.all().order_by('pk')
    return render(request, 'life/person_list.html', {'persons': persons})


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    events = person.event_set.all()
    pupils = person.pupil_set.all()
    return render(request, 'life/person_detail.html', {'person': person, 'events': events, 'pupils': pupils})


def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = PersonForm()
    return render(request, 'life/person_edit.html', {'form': form})


def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = PersonForm(instance=person)
    return render(request, 'life/person_edit.html', {'form': form})


def event_new(request, pk):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.person = get_object_or_404(Person, pk=pk)
            event.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = EventForm()
    return render(request, 'life/event_edit.html', {'form': form})


def event_edit(request, pk, ek):
    person = get_object_or_404(Person, pk=pk)
    event = get_object_or_404(Event, pk=ek)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'life/event_edit.html', {'form': form})

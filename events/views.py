from django.shortcuts import render
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm


def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venues.html', {
        'venue_list': venue_list,
    })

def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {
        'form': form,
        'submitted': submitted
    })


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'Jonh'
    month = month.capitalize()
    month_number = int(list(calendar.month_name).index(month))
    cal = HTMLCalendar().formatmonth(year, month_number)
    return render(request, 'events/home.html', {
        'name': name,
        'year': year,
        'month': month,
        'calendar': cal,
    })


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/events_list.html', {
        'event_list': event_list,
    })

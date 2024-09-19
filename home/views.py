from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

from schedule.models import Calendar

def calendar_view(request, calendar_slug):
    calendar = Calendar.objects.get(slug=calendar_slug)
    events = calendar.events.all()
    return render(request, 'schedule/calendar.html', {'calendar': calendar, 'events': events})

from django.urls import path

app_name = 'home'

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar', views.calendar_view, name='calendar'),
]

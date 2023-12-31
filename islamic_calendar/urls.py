from django.urls import path
from . import views

app_name = 'islamic_calendar'

urlpatterns = [
    path('', views.islamic_calendar, name='islamic_calendar'),
    path('<int:year>/', views.islamic_calendar, name='islamic_calendar_year'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='month'),
    path('events/', views.all_events, name='events_list'),
    path('add_venue', views.add_venue, name='add-venue'),
    path('list_venues/', views.list_venues, name='venues_list'),
]

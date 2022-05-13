from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField('Venue name', max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.CharField('Zip code', max_length=20)
    phone = models.CharField(max_length=30, blank=True)
    web = models.URLField(blank=True)
    email_address = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('event name', max_length=200)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    atendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name

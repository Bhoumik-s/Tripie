from __future__ import unicode_literals

from django.db import models
from signup.models import User
from Plan.models import MumbaiLocation

class ItineraryInput(models.Model):
	ItineraryInputId = models.AutoField(primary_key=True, default=0)
	UserId = models.ForeignKey(User)
	ItineraryName = models.CharField(max_length=20)
	StartTime = models.TimeField(default="09:00:00")
	EndTime = models.TimeField(default="17:00:00")
	StartLatitude = models.DecimalField(max_digits=10, decimal_places=7)
	StartLongitude = models.DecimalField(max_digits=10, decimal_places=7)
	EndLatitude = models.DecimalField(max_digits=10, decimal_places=7)
	EndLongitude = models.DecimalField(max_digits=10, decimal_places=7)
	ActiveItinerary = models.ForeignKey(Itinerary)

	def __str__(self):
		return str(self.ItineraryId) + str(self.UserId)

class Itinerary(models.Model):
	ItineraryId = models.AutoField(primary_key=True, default=0)
	ItineraryInputId = models.ForeignKey(ItineraryInput)
	CreatedOn = models.TimeField(default="09:00:00")

class ItineraryDestination(models.Model):
	ItineraryId = models.ForeignKey(ItineraryInput)
	LocationId = models.ForeignKey(MumbaiLocation)
	StartTime = models.TimeField(default="09:00:00")
	Duration = models.DurationField(default="00:30:00")

class ItineraryRoute(models.Model):
	ItineraryId = models.ForeignKey(ItineraryInput)
	RouteId = models.ForeignKey(MumbaiLocation)
	StartTime = models.TimeField(default="09:00:00")
	Duration = models.DurationField(default="00:30:00")
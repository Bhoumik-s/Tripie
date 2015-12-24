from django.db import models

# Create your models here.
class Mumbai_db(models.Model):

	placeId = models.PositiveSmallIntegerField()
	name = models.CharField(max_length=50)
	latitude = models.DecimalField(max_digits=10, decimal_places=7)
	longitude = models.DecimalField(max_digits=10, decimal_places=7)
	openTime = models.PositiveSmallIntegerField(help_text="minutes since 5AM")
	dueTime = models.PositiveSmallIntegerField(help_text="minutes since 5AM")
	serviceTime = models.PositiveSmallIntegerField(help_text="In minutes")
	
	defaultHappiness = models.PositiveSmallIntegerField()
	sightSeeing = models.PositiveSmallIntegerField()
	religious = models.PositiveSmallIntegerField()
	amusement = models.PositiveSmallIntegerField()
	nightLife = models.PositiveSmallIntegerField()
	shopping = models.PositiveSmallIntegerField()

	cost = models.PositiveSmallIntegerField()


	timings = models.CharField(max_length=20,help_text="e.g: 9:30 AM - 12:45 PM")
	description = models.TextField()
	comment1 = models.TextField()
	comment2 = models.TextField()

	def __str__(self):
		return self.name
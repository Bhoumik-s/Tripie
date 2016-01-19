from django.db import models

# Create your models here.
class MumbaiLocation(models.Model):
	LocationId = models.AutoField(primary_key=True, default=0)
	Name = models.CharField(max_length=100)
	Latitude = models.DecimalField(max_digits=10, decimal_places=7)
	Longitude = models.DecimalField(max_digits=10, decimal_places=7)
	OpenTime = models.TimeField(default="09:00:00")
	DueTime = models.TimeField(default="17:00:00")
	ServiceTime = models.DurationField(default="01:00:00")
	GeneralInfo = models.FilePathField(path = "./")
	Cost = models.PositiveIntegerField(default=0)
	# DaysOpen = models.
	# defaultHappiness = models.PositiveSmallIntegerField()
	# sightSeeing = models.PositiveSmallIntegerField()
	# religious = models.PositiveSmallIntegerField()
	# amusement = models.PositiveSmallIntegerField()
	# nightLife = models.PositiveSmallIntegerField()
	# shopping = models.PositiveSmallIntegerField()



	# timings = models.CharField(max_length=20,help_text="e.g: 9:30 AM - 12:45 PM")
	# description = models.TextField()
	# comment1 = models.TextField()
	# comment2 = models.TextField()

	def __str__(self):
		return self.Name

class Tag(models.Model):
	TagId = models.AutoField(primary_key = True, default = 0)
	TagName = models.CharField(max_length=50)
	TagInfo = models.CharField(max_length=200)
	def __str__(self):
		return self.TagName	

class MumbaiTagLocation(models.Model):
	TagId = models.ForeignKey("Tag")
	LocationId = models.ForeignKey("MumbaiLocation")
	Weightage = models.PositiveSmallIntegerField(default = 1)
	def __str__(self):
		return str(self.TagId) + "-" + str(self.LocationId )+ " : " + str(self.Weightage)

class Route(models.Model):
	RouteId = models.AutoField(primary_key=True, default=0)
	Destination1 = models.ForeignKey("MumbaiLocation", related_name = "Destination1")
	Destination2 = models.ForeignKey("MumbaiLocation", related_name = "Destination2")
	Slot11 = models.DurationField(default="00:30:00")
	Slot21 = models.DurationField(default="00:30:00")
	Slot31 = models.DurationField(default="00:30:00")
	Slot41 = models.DurationField(default="00:30:00")
	Slot51 = models.DurationField(default="00:30:00")
	Slot12 = models.DurationField(default="00:30:00")
	Slot22 = models.DurationField(default="00:30:00")
	Slot32 = models.DurationField(default="00:30:00")
	Slot42 = models.DurationField(default="00:30:00")
	Slot52 = models.DurationField(default="00:30:00")

	def __str__(self):
		return str(self.Destination1) + "-" + str(self.Destination2)

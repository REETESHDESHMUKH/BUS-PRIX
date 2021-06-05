from django.db import models

# Create your models here.
class Bus(models.Model):
    id = models.AutoField
    bus_name = models.CharField(max_length=50, default="")
    type = models.CharField(max_length=50,default="")
    number_seats = models.IntegerField(default="250")
    busConductor = models.CharField(max_length=50,default="")
    conductorContact = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.bus_name

class Passengers(models.Model):
    id = models.AutoField
    passenger_name = models.CharField(max_length=50,default="")
    image = models.ImageField(upload_to="ticket/images", default="")
    contact_no = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50,default="")
    email = models.EmailField(max_length=254,default="")
    password = models.CharField(max_length=30,default="")

    def __str__(self):
        return self.passenger_name

class Bus_stops(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50,default="")
    location = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name

class Schedules(models.Model):
    id = models.AutoField
    route = models.ForeignKey('Route',on_delete=models.CASCADE)
    time = models.DateField()

    def __str__(self):
        return self.time

class Bus_ticket(models.Model):
    id = models.AutoField
    sch_id = models.ForeignKey('Schedules',on_delete=models.CASCADE)
    pass_id = models.ForeignKey('Passengers',on_delete=models.CASCADE)

    def __str__(self):
            return (self.sch_id+" "+self.pass_id)

class Route(models.Model):
    id = models.AutoField
    bus_rou = models.ForeignKey('Bus', on_delete=models.CASCADE,default="")
    origin = models.CharField(max_length=50,default="")
    destination = models.CharField(max_length=50,default="")
    cost = models.IntegerField(default="250")


    def __str__(self):
        return (self.origin+" "+self.destination)

class Help(models.Model):
    id = models.AutoField
    Name = models.CharField(max_length=50,default="")
    Email = models.EmailField(max_length=254,default="")
    Message = models.CharField(max_length=250,default="")

    def __str__(self):
        return self.Name
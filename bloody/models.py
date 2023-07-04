from django.db import models
from django.contrib.auth.models import User

# Blood groups for `demande', `donate' class
BGs = [
    ('A+', 'A positive'),
    ('A-', 'A negative'),
    ('B+', 'B positive'),
    ('B-', 'B negative'),
    ('AB+', 'AB positive'),
    ('AB-', 'AB negative'),
    ('O+', 'O positive'),
    ('O-', 'O negative'),
]


class health_center(models.Model):
    def upload(instance, filename):
        return "center/{0}_{1}".format(instance.name, filename)

    name    = models.TextField(primary_key = True, max_length = 256)
    email   = models.EmailField()
    profile = models.ImageField(upload_to = upload)

class health_person(models.Model):
    def upload(instance, filename):
        return "person_{0}/{1}".format(instance.name, filename)

    user    = models.OneToOneField(User, on_delete = models.CASCADE)
    center  = models.ForeignKey(health_center, on_delete = models.CASCADE)
    tel     = models.TextField()
    email   = models.EmailField()
    profile = models.ImageField(upload_to = upload)

class demand(models.Model):
    blood_group = models.CharField(max_length = 3, choices = BGs)
    age         = models.PositiveIntegerField()
    sex         = models.CharField(max_length = 2)
    date        = models.DateTimeField()
    location    = models.TextField(blank = True)
    center      = models.ForeignKey(health_person, on_delete = models.CASCADE)

class donator(models.Model):
    def upload(instance, filename):
        return "donator_{0}/{1}".format(instance.name, filename)

    user    = models.OneToOneField(User, on_delete = models.CASCADE)
    name    = models.CharField(max_length = 256)
    tel     = models.TextField(max_length = 12)
    email   = models.EmailField()
    age     = models.PositiveIntegerField(blank = True)
    profile = models.ImageField(upload_to = upload)

class donate(models.Model):
    donator     = models.ForeignKey(donator, on_delete = models.CASCADE)
    center      = models.ForeignKey(health_person, on_delete = models.CASCADE)
    blood_group = models.CharField(max_length = 3, choices = BGs)
    age         = models.PositiveIntegerField()
    date        = models.DateTimeField()

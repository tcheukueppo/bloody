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

class bag(models.Model):
    blood_group = models.CharField(max_length = 3, choices = BGs)
    cost        = models.DecimalField()

class health_center(models.Model):
    def upload(instance, filename):
        return "center/{0}_{1}".format(instance.name, filename)

    name    = models.TextField(primary_key = True, max_length = 256)
    email   = models.EmailField()
    profile = models.ImageField(upload_to = upload)

class health_center_bags(models.Model):
    bag   = models.ForeignKey(bag, on_delete = models.CASCADE)
    hc    = models.ForeignKey(health_center, on_delete = models.CASCADE)
    count = models.PositiveIntegerField()

class health_person(models.Model):
    def upload(instance, filename):
        return "person_{0}/{1}".format(instance.name, filename)

    user    = models.OneToOneField(User, on_delete = models.CASCADE)
    center  = models.ForeignKey(health_center, on_delete = models.CASCADE)
    tel     = models.TextField()
    email   = models.EmailField()
    profile = models.ImageField(upload_to = upload)

class request_donation(models.Model):
    health_person = models.ForeignKey(health_person, on_delete = models.CASCADE)
    blood_group   = models.CharField(max_length = 3, choices = BGs)
    age           = models.PositiveIntegerField()
    sex           = models.CharField(max_length = 2)
    date          = models.DateTimeField()
    location      = models.TextField(blank = True)

class donor(models.Model):
    def upload(instance, filename):
        return "donor_{0}/{1}".format(instance.name, filename)

    user  = models.OneToOneField(User, on_delete = models.CASCADE)
    name  = models.CharField(max_length = 256)
    tel   = models.TextField(max_length = 12)
    email = models.EmailField()
    age   = models.PositiveIntegerField(blank = True)

class donate(models.Model):
    donor       = models.ForeignKey(donor, on_delete = models.CASCADE)
    hc          = models.ForeignKey(health_center, on_delete = models.CASCADE)
    blood_group = models.CharField(max_length = 3, choices = BGs)
    age         = models.PositiveIntegerField()
    date        = models.DateTimeField()
    number_bags = models.PositiveIntegerField()

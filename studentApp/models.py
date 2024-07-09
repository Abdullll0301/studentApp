from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Result(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    math = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    biology = models.IntegerField(default=0)
    irs = models.IntegerField(default=0)

    def __str__(self):
        return f"Results for {self.user.username}"

class SchoolItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='school_items')

    def __str__(self):
        return self.name

from distutils.command.upload import upload
from statistics import mode
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(models.Model):
    ticket = models.ForeignKey("Ticket", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = self.headline + ": " + self.ticket.title
        name = name[:128]
        return name

class Ticket(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='media/img')
    time_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

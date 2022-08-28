from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserTheme(models.Model):
    THEME_CHOICES = (
        ('cyborg', 'cyborg'),
        ('cerulean', 'cerulean'),
        ('quartz', 'quartz'),
        ('lumen', 'lumen'),
        ('simplex', 'simplex'),
        ('sketchy', 'sketchy'),
    )    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(choices=THEME_CHOICES, default='cyborg', max_length=10)

    def __str__(self):
        return "theme: " + self.user.username
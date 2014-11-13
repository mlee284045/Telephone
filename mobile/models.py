from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, name='profile')
    picture = models.ImageField(null=True)
    description = models.TextField(blank=True, null=True)


class Telephone(models.Model):
    pass
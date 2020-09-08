from django.db import models


# Create your models here.


class TwitUser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class NewTwitUser(models.Model):
    name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name

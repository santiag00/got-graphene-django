from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

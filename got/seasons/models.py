from django.db import models


class Season(models.Model):
    number = models.IntegerField()
    rating = models.FloatField()

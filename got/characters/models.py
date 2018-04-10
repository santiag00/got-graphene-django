from django.db import models


class Character(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_alive = models.BooleanField(default=False)
    origin = models.ForeignKey('places.Place', models.DO_NOTHING)
    seasons = models.ManyToManyField('seasons.Season')

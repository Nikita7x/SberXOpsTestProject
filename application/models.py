from django.db import models


class Activity(models.Model):
    domain = models.CharField(max_length=250)
    datetime = models.DateTimeField()

from django.db import models
from django.utils import timezone


class Coffee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.FloatField()


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(default=timezone.now)
    item = models.ForeignKey(Coffee, on_delete=models.PROTECT)
    pre_tax = models.FloatField()
    tax = models.FloatField()

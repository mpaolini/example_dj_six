from django.db import models


class Item(models.Model):
    key = models.CharField(max_length=100, primary_key=True)
    value = models.TextField()


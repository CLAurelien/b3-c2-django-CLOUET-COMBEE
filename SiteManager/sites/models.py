from django.db import models


class Sites(models.Model):
    name = models.CharField(max_length=40),
    address = models.CharField(max_length=100),
    password = models.CharField(max_length=30)

from django.db import models


class Sites(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100, blank=True)
    id_email = models.CharField(max_length=60)
    password = models.CharField(max_length=30)

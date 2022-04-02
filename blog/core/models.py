from django.db import models


class Subscriber(models.Model):
    email = models.CharField(unique=True, max_length=50)

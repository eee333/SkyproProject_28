from django.db import models


class Adv(models.Model):
    text = models.CharField(max_length=1000)

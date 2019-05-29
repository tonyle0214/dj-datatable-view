from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=32, null=False)
    age = models.PositiveIntegerField(null=False)

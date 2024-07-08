from django.db import models

# Create your models here.

class Human(models.Model):

    name = models.CharField('Human name', max_length=60)
    age = models.PositiveIntegerField('Human age')

    def __str__(self):
        return self.name
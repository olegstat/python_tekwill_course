from django.db import models

# Create your models here.

class FancyCat(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('date_added', )

class FluffyTiger(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    color = models.CharField(max_length=255)
    birth_date = models.CharField(max_length=255)
    rare = models.BooleanField(default=False)

    class Meta:
        ordering = ('date_added', )

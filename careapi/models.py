from django.db import models

# Create your models here.
class Office(models.Model):
    name = models.CharField(max_length=200)
    staff_rating = models.IntegerField(default=0)
    forms_language = models.IntegerField(default=0)

class Provider(models.Model):
    name = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=5)
    provider_type = models.CharField(max_length=200)
    office_id = models.ForeignKey(
        Office,
        models.SET_NULL,
        blank=True,
        null=True,
    )

class Permission(models.Model):
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=200)
    access_level = models.IntegerField(default=0)
from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ('erkak', 'erkak'),
    ('ayol', 'ayol')
)

ROLE_CHOICES = (
    ('seller', 'seller'),
    ('client', 'client'),
)


class Profile(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True)
    card = models.CharField(max_length=20, blank=True, null=True)

    firm_name = models.CharField(max_length=255, blank=True, null=True)
    firm_file = models.FileField(upload_to='firm_file', blank=True, null=True)

    def __str__(self):
        return f"{self.phone}"

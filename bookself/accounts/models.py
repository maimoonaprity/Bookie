# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('author', 'Author'),
        ('visitor', 'Visitor'),
        
    )
    name = models.CharField(max_length=255, blank=True, null=True) 
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='visitor')



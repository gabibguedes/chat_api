from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, null=False)
    first_name = models.CharField(max_length=255, blank=True, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    USERNAME_FIELD = username

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name}"

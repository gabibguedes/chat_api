from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')        
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)
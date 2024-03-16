from django.db import models

# Create your models here.

class ReminderData(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=20, choices=[('SMS', 'SMS'), ('Email', 'Email')])

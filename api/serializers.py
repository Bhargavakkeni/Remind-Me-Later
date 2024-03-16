from rest_framework import serializers
from .models import ReminderData

class ReminderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReminderData
        fields = ['id', 'date', 'time', 'message', 'reminder_type']
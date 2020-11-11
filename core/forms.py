from django.forms import ModelForm

from .models import (
    Message,
    PrayerRequest)

class MessageForm(ModelForm):
    pass

class PrayerRequestForm(ModelForm):
    class Meta:
        model = PrayerRequest
        fields = '__all__'
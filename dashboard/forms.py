from django import forms
from .models import Plant


class SettingsForm(forms.ModelForm):
    sunrise = forms.DateTimeField(input_formats=["%H:%M"], widget=forms.TimeInput(
        attrs={
            'class': 'form-control datetimepicker-input'
        }
    ))
    sunset = forms.DateTimeField(input_formats=["%H:%M"], widget=forms.TimeInput(
        attrs={
            'class': 'form-control datetimepicker-input'
        }
    ))
    feed = forms.DateTimeField(input_formats=["%H:%M"],  widget=forms.TimeInput(
        attrs={
            'class': 'form-control datetimepicker-input'
        }
    ))
    plant = forms.IntegerField()

    class Meta:
        model = Plant
        fields = ('sunrise', 'sunset', 'feed', 'plant',)
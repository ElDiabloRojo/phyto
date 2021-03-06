from django import forms
from .models import Setting


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

    class Meta:
        model = Setting
        fields = ('sunrise', 'sunset', 'feed',)
from django.db import models

# Create your models here.
class Plant(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    sunrise = models.TimeField(null=True)
    sunset = models.TimeField(null=True)
    feed = models.TimeField(null=True)

    def __int__(self):
        return self.id
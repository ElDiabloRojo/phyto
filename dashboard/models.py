from django.db import models

# Create your models here.
class Plant(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Setting(models.Model):
    plant = models.ForeignKey(Plant, default=None, on_delete=models.CASCADE)
    sunrise = models.DateField()
    sunset = models.DateField()
    feed = models.DateField()
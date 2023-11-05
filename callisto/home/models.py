from django.db import models

# Create your models here.
class History(models.Model):
    user = models.BooleanField(default=False)
    chat = models.CharField(max_length=300)
    
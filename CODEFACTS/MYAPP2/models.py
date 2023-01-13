from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=1224)
    email=models.CharField(max_length=50)
    desc=models.CharField(max_length=122225)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class std_data(models.Model):
    username = models.CharField(max_length=80)
    email = models.EmailField()
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.username
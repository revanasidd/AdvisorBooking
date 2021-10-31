from django.db import models

class UserModel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.username


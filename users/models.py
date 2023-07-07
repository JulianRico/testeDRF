from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    about = models.TextField()
    pictureurl = models.URLField()
    position = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

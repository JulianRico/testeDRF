from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    about = models.TextField()
    pictureurl = models.URLField(
        default='https://firebasestorage.googleapis.com/v0/b/data-qc-api.appspot.com/o/profiles%2FQC_logo.jpeg?alt=media&token=a8577eee-215a-4b33-9b61-7c764a4eb171')
    position = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

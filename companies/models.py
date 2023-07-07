from django.db import models
# from reports.models import Report
# Create your models here.


class Companie(models.Model):
    name = models.CharField(max_length=500)
    nit = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    manager = models.CharField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

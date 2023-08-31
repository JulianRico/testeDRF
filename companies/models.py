from django.db import models
# from reports.models import Report
# Create your models here.


class Companie(models.Model):
    name = models.CharField(max_length=500)
    nit = models.CharField(max_length=30)
    email = models.EmailField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserCompany(models.Model):
    usuario = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)   
    contact = models.CharField(max_length=200)
    emailContact = models.EmailField()
    create_at = models.DateTimeField(auto_now_add=True)
    companie = models.ForeignKey(Companie, related_name='users',
                                 on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.usuario

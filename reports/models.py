from django.db import models
from users.models import User
from companies.models import Companie

# Create your models here.


class Report(models.Model):
    questionsmtto = models.JSONField()
    questionviews = models.JSONField()
    questionsdeterioration = models.JSONField()
    SelfStatus = ((1, "Espera"), (2, "Rechazado"), (3, "Aprobado"))
    status = models.IntegerField(choices=SelfStatus, default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='reports',
                             on_delete=models.CASCADE, blank=True, null=True)
    companie = models.ForeignKey(
        Companie, related_name='reports', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)

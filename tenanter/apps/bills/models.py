from django.db import models
from tenanter.apps.flat.models import Flat


class Bills_agreement(models.Model):
    flat = models.ForeignKey(
        Flat, related_name='bills_agreement', on_delete=models.CASCADE)  # TODO: index
    name = models.CharField(max_length=40)
    rate = models.FloatField()
    is_dynamic = models.BooleanField()

    def __str__(self):
        return f'{self.flat_id}, {self.name} {self.rate}'

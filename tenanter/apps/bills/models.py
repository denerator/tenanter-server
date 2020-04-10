"""Bills model declarations"""
from django.db import models
from tenanter.apps.flat.models import Flat, Tenant


class BillsAgreement(models.Model):
    """Bills agreement model"""
    flat = models.ForeignKey(
        Flat, related_name='bills_agreement', on_delete=models.CASCADE)  # TODO: index
    name = models.CharField(max_length=40)
    rate = models.FloatField()
    is_dynamic = models.BooleanField()

    def __str__(self):
        return self.name


class BillsHistory(models.Model):
    """Bills history model"""
    flat = models.ForeignKey(
        Flat, related_name='bills_history', on_delete=models.CASCADE)  # TODO: index
    date = models.DateField()  # TODO: index
    bill = models.ForeignKey(
        BillsAgreement, related_name='bills_history', on_delete=models.CASCADE)  # TODO: index
    rate = models.FloatField()
    value = models.IntegerField(blank=True, null=True)
    difference = models.IntegerField(blank=True, null=True)
    total = models.FloatField()

    def __str__(self):
        return self.bill

class PaymentHistory(models.Model):
    """Payment history model"""
    date = models.DateField()
    flat = models.ForeignKey(
        Flat, related_name='payment_history', on_delete=models.CASCADE)  # TODO: index
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    bills = models.FloatField()
    rental_rate = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return self.total

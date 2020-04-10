"""Flat models declarations"""
from django.db import models
from tenanter.apps.user.models import User


class Flat(models.Model):
    """Flat model"""
    address = models.CharField(max_length=60, unique=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owned_flats')

    def __str__(self):
        return f'{self.address}, {self.owner}'


class Tenant(models.Model):
    """Tenant model"""
    signing_date = models.DateField()
    payment_day = models.IntegerField()
    contract_time = models.IntegerField()
    rental_rate = models.IntegerField()
    deposit = models.IntegerField()
    flat = models.OneToOneField(
        Flat, on_delete=models.CASCADE, related_name='tenant')
    name = models.CharField(max_length=30)  # For MVP we leave these fields
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name

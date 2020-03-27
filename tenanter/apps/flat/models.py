from django.db import models
from tenanter.apps.user.models import User


class Flat(models.Model):
    address = models.CharField(max_length=60)
    owner_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner')
    tenant_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tenant')

    def __str__(self):
        return f'{self.address}, {self.owner_id}'


class Tenant(models.Model):
    signingDate = models.DateField()
    paymentDay = models.IntegerField()
    contractTime = models.IntegerField()
    rental_rate = models.IntegerField()
    deposit = models.IntegerField()
    flat_id = models.ForeignKey(
        Flat, unique=True, on_delete=models.CASCADE, related_name='flat')
    tenant_id = models.ForeignKey(
        User, unique=True, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f'{self.flat_id}, {self.tenant_id}'


class Bills_agreement(models.Model):
    flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE)  # index
    name = models.CharField(max_length=40)
    rate = models.IntegerField()
    is_dynamic = models.BooleanField()

    def __str__(self):
        return f'{self.flat_id}, {self.name} {self.rate}'


class Bills_history(models.Model):
    flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE)
    date = models.DateField()  # index
    name = models.CharField(max_length=40)
    rate = models.IntegerField()
    value = models.IntegerField()
    difference = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f'{self.flat_id}, {self.date} {self.name} {self.rate}'


class Payment_history(models.Model):
    date = models.DateField()
    flat_id = models.IntegerField()
    tenant_id = models.IntegerField()
    bills = models.IntegerField()
    rental_rate = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f'{self.flat_id}, {self.date} {self.bills} {self.total}'

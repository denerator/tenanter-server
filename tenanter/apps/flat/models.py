from django.db import models
from tenanter.apps.user.models import User


class Flat(models.Model):
    address = models.CharField(max_length=60, unique=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owned_flats')

    def __str__(self):
        return f'{self.address}, {self.owner}'


class Tenant(models.Model):
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
        return f'{self.deposit}, {self.name}, {self.phone}'


class Bills_history(models.Model):
    flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE)
    date = models.DateField()  # TODO: index
    name = models.CharField(max_length=40)
    rate = models.IntegerField()
    value = models.IntegerField()
    difference = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f'{self.flat_id}, {self.date} {self.name} {self.rate}'


class Payment_history(models.Model):
    date = models.DateField()
    flat_id = models.IntegerField()  # TODO: index
    tenant_id = models.IntegerField()
    bills = models.IntegerField()
    rental_rate = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f'{self.flat_id}, {self.date} {self.bills} {self.total}'

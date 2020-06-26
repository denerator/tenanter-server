from django.contrib import admin
from .models import BillsAgreement, BillsHistory, PaymentHistory

admin.site.register(BillsAgreement)
admin.site.register(BillsHistory)
admin.site.register(PaymentHistory)

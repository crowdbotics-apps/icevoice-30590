from django.contrib import admin
from .models import Order, Bill, PaymentMethod

admin.site.register(Order)
admin.site.register(Bill)
admin.site.register(PaymentMethod)

# Register your models here.

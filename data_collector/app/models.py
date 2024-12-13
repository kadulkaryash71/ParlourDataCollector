from django.db import models

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=255, blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_name

class Transaction(models.Model):
    customer_name = models.CharField(max_length=255, blank=True, null=True, default="Anonymous")
    transaction_cost = models.IntegerField(null=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service_transaction")

    def __str__(self):
        return f"{self.date_created}_{self.customer_name}-{self.service.service_name}"

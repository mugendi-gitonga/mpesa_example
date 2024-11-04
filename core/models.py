from django.db import models

# Create your models here.

class STKPushRequest(models.Model):
    phone_number = models.CharField(max_length=12)
    amount = models.IntegerField()
    trans_ref = models.CharField(max_length=11, null=True, blank=True)
    description = models.CharField(max_length=30, null=True, blank=True)
    stk_resp = models.JSONField( null=True, blank=True)

class MpesaDepositTransaction(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('VALIDATING', 'VALIDATING'),
        ('SUCCESS', 'SUCCESS'),
        ('FAILED', 'FAILED')
    ]

    phone_number = models.CharField(max_length=15)
    acc_number = models.CharField(max_length=15)
    names = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=20, unique=True)
    amount = models.IntegerField()
    trans_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '%s, %s, %s' % (self.transaction_id, self.acc_number, self.status)
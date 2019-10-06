from django.db import models
from datetime import datetime
# Create your models here.


class EmailTable(models.Model):
    receiver = models.CharField(max_length=1000, null=True, blank=True)
    subject = models.CharField(max_length=1000, null=True, blank=True)
    body = models.CharField(max_length=5000, null=True, blank=True)
    cc = models.CharField(max_length=1000, null=True, blank=True)
    bcc = models.CharField(max_length=1000, null=True, blank=True)
    timestamp = models.DateField(default=datetime.now())


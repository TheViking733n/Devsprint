from django.db import models

class FeesPayments(models.Model):
    id = models.BigIntegerField(primary_key = True)
    name = models.CharField(max_length=100)
    entry = models.CharField(max_length=12)
    semester = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    # payment_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.entry
from django.db import models

class CurrencyRate(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    rate = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - {self.rate}"

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    used = models.BooleanField(default=False)
    price = models.IntegerField()
    
    def __str__(self):
        return self.title


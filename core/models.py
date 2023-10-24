from django.db import models

# Create your models here.

class PalindromeGame(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True, default="")
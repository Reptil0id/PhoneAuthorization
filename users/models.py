from django.db import models

# Create your models here.

class ReferralModel(models.Model):
    CreatedAt = models.DateTimeField(
        verbose_name='Дата создания', auto_now_add=True, null=True)
    PhoneNumber = models.CharField(max_length=20, blank=True, unique=True)
    Code = models.CharField(max_length=6, null=True, blank=True)
    ReferralCode = models.CharField(max_length=6, null=True, blank=True)

class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
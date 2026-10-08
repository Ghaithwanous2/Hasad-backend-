from django.conf import settings
from django.db import models


class Field(models.Model):
    farmer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="fields",
    )

    name = models.CharField(
        max_length=150,
    )

    location = models.CharField(max_length=255)

    latitude = models.DecimalField(
         max_digits=9,
        decimal_places=6,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )


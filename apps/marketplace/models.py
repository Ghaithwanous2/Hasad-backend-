from django.conf import settings
from django.contrib.gis.db import models


class Field(models.Model):
    farmer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="fields",
    )

    name = models.CharField(max_length=150)

    location = models.PointField(
        geography=True,
        srid=4326,
    )

    address = models.CharField(
        max_length=255,
        blank=True,
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
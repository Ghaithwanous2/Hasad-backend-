import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("The phone number must be provided.")

        user = self.model(
            phone=phone,
            **extra_fields,
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        if not password:
            raise ValueError("Superuser must have a password.")

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", self.model.Role.ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            phone=phone,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):

    class Role(models.TextChoices):
        FARMER = "FARMER", "Farmer"
        TRADER = "TRADER", "Trader"
        DELIVERY_MANAGER = "DELIVERY_MANAGER", "Delivery manager"
        DRIVER = "DRIVER", "Driver"
        WAREHOUSE_MANAGER = "WAREHOUSE_MANAGER", "Warehouse manager"
        INSPECTOR = "INSPECTOR", "Neutral inspector"
        QUALITY_MANAGER = "QUALITY_MANAGER", "Quality manager"
        ADMIN = "ADMIN", "Administrator"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    phone = models.CharField(
        max_length=30,
        unique=True,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    role = models.CharField(
        max_length=32,
        choices=Role.choices,
    )

    status = models.CharField(
        max_length=20,
        default="ACTIVE",
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "phone"
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
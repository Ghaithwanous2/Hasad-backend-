
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import FarmerProfile, TraderProfile, User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        "phone",
        "first_name",
        "last_name",
        "email",
        "role",
        "status",
        "is_active",
        "is_staff",
    )

    ordering = ("-created_at",)

    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "role",
                    "status",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "first_name",
                    "last_name",
                    "email",
                    "role",
                    "status",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "last_login",
    )
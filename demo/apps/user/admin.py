from django.contrib import admin
from demo.apps.user.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "score"
    )
    search_fields = ("pk", "first_name", "last_name", "email")


admin.site.site_header = "demo"

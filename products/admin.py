from django.contrib import admin
from .models import Course, Artist, Order

admin.site.register(Course)
admin.site.register(Artist)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "course", "date_order", "people", "get_total"]

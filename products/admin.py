from django.contrib import admin
from .models import Course, Artist, Order

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "price","date_start","teacher"]
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "course", "date_order", "people", "get_total"]

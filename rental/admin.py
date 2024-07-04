from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bike, Rental

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_available')
    search_fields = ('name', 'description')
    list_filter = ('is_available',)

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('bike', 'user', 'start_time', 'end_time')
    search_fields = ('bike__name', 'user__username')
    list_filter = ('start_time', 'end_time')

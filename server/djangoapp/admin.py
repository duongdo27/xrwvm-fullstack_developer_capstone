from django.contrib import admin
from .models import CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['CarModel', 'CarMake']

# Register models here
admin.site.register(CarModel)
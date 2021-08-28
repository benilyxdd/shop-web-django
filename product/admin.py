from django.contrib import admin
from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'date_modified')
    search_fields = ['name']
    readonly_fields = ('date_created', 'date_modified')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

from django.contrib import admin
from .models import MenuItem,Category

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name','price']

admin.site.register(MenuItem,MenuItemAdmin)
admin.site.register(Category)
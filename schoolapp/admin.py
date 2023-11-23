from django.contrib import admin
from .models import Department, Course, Order, Material

admin.site.register(Department)
admin.site.register(Course)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'gender', 'display_materials_provided', 'phone_number', 'email', 'address', 'department', 'course', 'purpose')

    def display_materials_provided(self, obj):
        return ", ".join([material.name for material in obj.materials_provided.all()])
    
    display_materials_provided.short_description = 'Materials Provided'  # Set a custom column header

admin.site.register(Order, OrderAdmin)

from django.contrib import admin
from .models import Category, Villa, Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'created_date')
    search_fields = ('full_name', 'email')
    list_filter = ('created_date', )

admin.site.register(Category)
admin.site.register(Villa)
admin.site.register(Lead, LeadAdmin)
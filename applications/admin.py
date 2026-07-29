from django.contrib import admin
from .models import Application, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'role', 'status', 'applied_date', 'user']
    list_filter = ['status', 'applied_date']
    search_fields = ['company', 'role']
    filter_horizontal = ['tags']
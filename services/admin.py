from django.contrib import admin
from .models import Service, RequestService

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')

@admin.register(RequestService)
class RequestServiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'status', 'requested_date')
    list_filter = ('status',)
    search_fields = ('user__username', 'service__name')

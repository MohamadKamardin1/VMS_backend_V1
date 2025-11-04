from django.contrib import admin
from .models import Office, Visitor, Visit

# Register your models here.
@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_person', 'contact_phone')
    search_fields = ('name', 'location', 'contact_person')
@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'nida_number', 'passport_number', 'phone', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'nida_number', 'passport_number', 'email')
    list_filter = ('created_at',)
@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'office', 'check_in_time', 'check_out_time', 'status')
    search_fields = ('visitor__first_name', 'visitor__last_name', 'office__name')
    list_filter = ('status', 'check_in_time', 'check_out_time')
    raw_id_fields = ('visitor', 'office')


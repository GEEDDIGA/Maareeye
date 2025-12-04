from django.contrib import admin
from .models import Patient, Doctor, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date_of_birth', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at', 'date_of_birth')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone', 'date_of_birth', 'address')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'email', 'phone', 'created_at')
    search_fields = ('name', 'specialization', 'email')
    list_filter = ('specialization', 'created_at')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Professional Information', {
            'fields': ('name', 'specialization', 'email', 'phone')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'status', 'created_at')
    search_fields = ('patient__name', 'doctor__name')
    list_filter = ('status', 'appointment_date', 'created_at')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Appointment Details', {
            'fields': ('doctor', 'patient', 'appointment_date', 'status')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

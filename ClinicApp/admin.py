from django.contrib import admin
from ClinicApp.models import CustomUser, Document, Appointment, Instrument

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = (
        "user_id",
        "mobile_number",
        "first_name",
        "last_name",
        "email"
    )
    list_display = (
        "user_id",
        "mobile_number",
        "first_name",
        "last_name",
        "email",
        "user_type",
        "is_staff",
        "is_active",
        "created_date",
        "updated_date"
    )

admin.site.register(CustomUser, CustomUserAdmin)

class DocumentAdmin(admin.ModelAdmin):
    search_fields = (
        "user__user_id",
        "user__email",
        "user__mobile_number",
        "doc_type",
        "name"
    )

    list_display = (
        "user",
        "name",
        "doc_type",
        "file",
        "disease",
        "created_date",
        "updated_date"
    )

admin.site.register(Document, DocumentAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    search_fields = (
        "appointment_id",
        "user__user_id",
        "user__email",
        "user__mobile_number"
    )

    list_display = (
        "appointment_id",
        "user",
        "appointment_date",
        "appointment_time",
        "created_date",
        "updated_date"
    )

admin.site.register(Appointment, AppointmentAdmin)

class InstrumentAdmin(admin.ModelAdmin):
    search_fields = (
        "name",
        "company",
        "type"
    )

    list_display = (
        "name",
        "company",
        "type",
        "cost",
        "order_on",
        "order_status",
        "remark",
        "created_date",
        "updated_date"
    )

admin.site.register(Instrument, InstrumentAdmin)
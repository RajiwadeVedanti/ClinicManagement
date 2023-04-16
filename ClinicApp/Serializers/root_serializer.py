from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ClinicApp.models import CustomUser, Document, Appointment


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = (
            "name",
            "doc_type",
            "file",
            "disease",
            "additional_data"
        )

class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            "appointment_id",
            "appointment_date",
            "appointment_time"
        )


class CustomUserListSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "user_id",
            "first_name",
            "last_name",
            "user_type",
            "mobile_number",
            "email",
            "dob",
            "address"
        )



class CustomUserDetailsSerializer(ModelSerializer):

    document = SerializerMethodField()
    appointment = SerializerMethodField()

    def get_document(self, user: CustomUser):
        data = user.document_uploaded_by_user.all()
        return DocumentSerializer(data, many=True).data
        
    def get_appointment(self, user: CustomUser):
        data = user.appointment_by_user.all()
        return AppointmentSerializer(data, many=True).data

    
    class Meta:
        model = CustomUser
        fields = (
            "user_id",
            "first_name",
            "last_name",
            "user_type",
            "mobile_number",
            "email",
            "dob",
            "address",
            "document",
            "appointment",
        )


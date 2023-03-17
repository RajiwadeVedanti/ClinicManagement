from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ClinicApp.models import CustomUser

class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_id"] = user.user_id
        token["mobile_number"] = user.mobile_number
        token["email"] = user.email
        return token
    
def get_token_pair(user: CustomUser) -> dict:
    token = CustomObtainPairSerializer.get_token(user)
    return {"access_token": str(token.access_token), "refresh_token": str(token)}
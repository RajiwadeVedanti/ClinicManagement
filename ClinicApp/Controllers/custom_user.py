from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ClinicApp.Repositories.custom_user import CustomUserRepository
from ClinicApp.Serializers.token_serializer import get_token_pair
from ClinicApp.helpers.model_search import get_or_none
from ClinicApp.models import CustomUser

class CustomUserController:
    @api_view(["POST"])
    def register(request):
        post_data = request.data
        success, message = CustomUserRepository.create_user(post_data)
        if not success:
            JsonResponse({"code":400, "response":message})
        return JsonResponse({"code":200, "response":message})
    

    @api_view(["POST"])
    def login(request):
        post_data = request.data
        username = post_data.get("username")
        password = post_data.get("password")

        if username.isdigit() and len(username) == 10:
            user = get_or_none(CustomUser, mobile_number = username, is_active = True )
        else:
            user = get_or_none(CustomUser, email__iexact = username, is_active = True )

        if not user:
            return JsonResponse({"code" :403, "response":"Invalid Credentials"})

        authentication = authenticate(username=user.mobile_number, password=password)
        if not authentication:
            return JsonResponse({"code" :403, "response":"Invalid Credentials"})
        tokens = get_token_pair(user)
        return JsonResponse(tokens)
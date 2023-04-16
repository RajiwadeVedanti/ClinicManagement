from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from ClinicApp.Repositories.custom_user import CustomUserRepository
from ClinicApp.Serializers.token_serializer import get_token_pair
from ClinicApp.helpers.model_search import get_or_none
from ClinicApp.helpers.decorator import validate_user
from ClinicApp.models import CustomUser

class CustomUserController:
    @api_view(["POST"])
    def register(request):
        post_data = request.data
        success, message = CustomUserRepository.create_user(post_data)
        if not success:
            return JsonResponse({"code":400, "response":message})
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
    
    @api_view(["GET"])
    def get_users(request):
        user_type = request.GET.get("user_type")
        success, response = CustomUserRepository(is_superuser=False,many=True).get_users(user_type=user_type)
        if not success:
            return JsonResponse({"code":404, "response":response})
        return JsonResponse({"code":200, "response":response})


    @api_view(["GET"])
    # @validate_user
    def get_user_details(request):
        # print("req user : ",request.user)
        user_id = request.GET.get("user_id")
        if not user_id:
            return JsonResponse({"code":400, "response": "UserID is required"})
        
        success, response = CustomUserRepository(user_id=user_id).get_user_details()
        if not success:
            return JsonResponse({"code":404, "response":response})
        return JsonResponse({"code":200, "response":response})
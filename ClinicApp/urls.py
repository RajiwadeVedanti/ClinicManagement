from django.urls import path
from ClinicApp.views import CustomUserController

urlpatterns = [
    path("register", CustomUserController.register, name="register_user"),
    path("login",CustomUserController.login,name="login_user"),

    path("user/list",CustomUserController.get_users,name="get_users"),
    path("user/details",CustomUserController.get_user_details,name="get_user_details")
]
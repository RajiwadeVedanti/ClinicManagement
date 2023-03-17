from django.urls import path
from ClinicApp.views import CustomUserController

urlpatterns = [
    path("register", CustomUserController.register, name="register_user"),
    path("login",CustomUserController.login,name="login_user"),
]
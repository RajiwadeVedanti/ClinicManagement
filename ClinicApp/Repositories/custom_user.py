from datetime import datetime
from django.db.models import QuerySet, Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from ClinicApp.models import CustomUser

class CustomUserRepository:
    def __init__(
        self,
        *args,
        item: CustomUser = None,
        many: bool = False,
        item_list: QuerySet = None,
        **kwargs
    ):
        super(CustomUserRepository, self).__init__(
            *args, item=item, many=many, item_list=item_list, **kwargs
        )   
    
    @staticmethod
    def create_user(post_data):
        try:
            first_name = post_data.get("first_name")
            last_name = post_data.get("last_name")
            mobile_number = post_data.get("mobile_number")
            email = post_data.get("email")
            password = post_data.get("password")
            address = post_data.get("address")
            dob = post_data.get("dob")
            user_type = post_data.get("user_type")
            is_staff = False

            if user_type in ("DOCTOR","RECEPTIONIST"):
                is_staff = True
            
            if dob:
                dob = datetime.strptime(dob,"%d/%m/%Y")

            query = Q()
            if email:
                query |= Q(email__iexact=email)
            if mobile_number:
                if isinstance(mobile_number,int):
                    mobile_number = str(mobile_number) 
                query |= Q(mobile_number=mobile_number)

            existing_user = CustomUser.objects.filter(query)

            if existing_user:
                return False, "Mobile / Email already exists."

            user = CustomUser.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                mobile_number = mobile_number,
                password = password,
                email = email,
                address = address,
                dob = dob,
                user_type = user_type,
                is_staff = is_staff
            )
            user.save()
                
            return True, "Account created successfully."
        except Exception as err:
            print("Error: ",err)
            return False, "Something went wrong"

    
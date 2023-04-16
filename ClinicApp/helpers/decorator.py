import json

def validate_user(func):
    def wrapper_func(request):
        user = request.user
        print("decorator user : ",user)
        return func
    return wrapper_func
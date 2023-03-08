from datetime import datetime
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import CharField, EmailField ,DateField, BooleanField, JSONField, IntegerField, FileField ,ForeignKey
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from simple_history.models import HistoricalRecords
from helpers.base import random_string_generator

def generate_user_id():
    return random_string_generator(length=10, digits=True, alphabets=True)

def generate_appointment_id():
    return random_string_generator(length=5, digits=True)

def get_user_document_filepath(instance, name):
    date = datetime.strftime(datetime.now(), "%Y/%m/%d/")
    ext = name.split(".")[-1]
    return "documents/" + date + instance.doc_type + "." + ext

class CustomUserManager(BaseUserManager):
    def create_user(self,mobile_number,password,**extra_fields):
        if not mobile_number:
            raise ValueError("Mobile Number is Required")
        
        user = self.model(mobile_number=mobile_number,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,mobile_number,password,**extra_fields):
        user = self.create_user(mobile_number,password,**extra_fields)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
        

class CustomUser(AbstractBaseUser,PermissionsMixin):
    user_type_choices = (
        ("DOCTOR","DOCTOR"),
        ("RECEPTIONIST","RECEPTIONIST"),
        ("PATIENT","PATIENT"),
        ("MR","MR")
    )
    user_id = CharField(max_length=10,unique=True,default=generate_user_id)
    first_name = CharField(max_length=255,null=True,blank=True)
    last_name = CharField(max_length=255,null=True,blank=True)
    mobile_number = CharField(max_length=10,unique=True)
    email = EmailField(max_length = 200, unique=True,null=True,blank=True)
    password = CharField(max_length=255)
    user_type = CharField(max_length=100,choices=user_type_choices,null=True,blank=True,default="PATIENT")
    dob = DateField(null=True,blank=True)
    address = CharField(max_length=255,null=True,blank=True)
    additional_data = JSONField(null=True,blank=True,default=dict)
    is_staff = BooleanField(default=False,verbose_name="Staff")
    is_admin = BooleanField(default=False,verbose_name="Admin")
    is_active = BooleanField(default=True,verbose_name="Active")
    history = HistoricalRecords()
    created_date = CreationDateTimeField()
    updated_date = ModificationDateTimeField()

    USERNAME_FIELD = "mobile_number"
    REQUIRED_FIELDS = ["mobile_number"]

    objects = CustomUserManager()

    def get_age(self):
        if self.dob:
            age = datetime.now().year - self.dob.year
            return age
    
    def __str__(self):
        return self.mobile_number or ""
    
class Document(models.Model):
    document_type = (
        ("PRESCIPTION","PRESCIPTION"),
        ("TSET","TEST")
    )
    patient = ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="document")
    doc_type = CharField(choices=document_type,null=True,blank=True,default="PRESCIPTION")
    file = FileField(upload_to=get_user_document_filepath,null=True,blank=True)
    disease = CharField(max_length=255,null=True,blank=True)
    additional_data = JSONField(null=True,blank=True,default=list)
    created_date = CreationDateTimeField()
    updated_date = ModificationDateTimeField()

    def __str__(self):
        return self.patient.mobile_number or ""


class Appointment(models.Model):
    appointment_id = CharField(max_length=10,default=generate_appointment_id)
    appointment_by = ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="appointment")
    appointment_date = DateField(null=True,blank=True)
    appointment_time = CharField(max_length=10,null=True,blank=True)
    created_date = CreationDateTimeField()
    updated_date = ModificationDateTimeField()

    def __str__(self):
        return self.appointment_by.mobile_number or ""
    
class Instrument(models.Model):
    type_choice = (
        ("MEDICINE","MEDICINE"),
        ("MACHINE","MACHINE")
    )
    name = CharField(max_length=255,null=True,blank=True)
    company = CharField(max_length=255,null=True,blank=True)
    type = CharField(choices=type_choice,null=True,blank=True,default="MEDICINE")
    cost = IntegerField(max_length=10,null=True,blank=True)
    order_on =  DateField(null=True,blank=True)
    created_date = CreationDateTimeField()
    updated_date = ModificationDateTimeField()

    def __str__(self):
        return self.type + " : " + self.name or ""



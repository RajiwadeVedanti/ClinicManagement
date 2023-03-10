# Generated by Django 4.1.4 on 2023-03-12 12:34

import ClinicApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, choices=[('MEDICINE', 'MEDICINE'), ('MACHINE', 'MACHINE')], default='MEDICINE', max_length=255, null=True)),
                ('cost', models.IntegerField(blank=True, default=0, null=True)),
                ('order_on', models.DateField(blank=True, null=True)),
                ('order_status', models.CharField(default='NEW', max_length=255, null=True)),
                ('remark', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.CharField(default=ClinicApp.models.generate_user_id, max_length=10, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True, unique=True)),
                ('is_email_varified', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=255, null=True)),
                ('user_type', models.CharField(blank=True, choices=[('DOCTOR', 'DOCTOR'), ('RECEPTIONIST', 'RECEPTIONIST'), ('PATIENT', 'PATIENT'), ('MR', 'MR')], default='PATIENT', max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_data', models.JSONField(blank=True, default=dict, null=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalCustomUser',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.CharField(db_index=True, default=ClinicApp.models.generate_user_id, max_length=10, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_number', models.CharField(db_index=True, max_length=10)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=200, null=True)),
                ('is_email_varified', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=255, null=True)),
                ('user_type', models.CharField(blank=True, choices=[('DOCTOR', 'DOCTOR'), ('RECEPTIONIST', 'RECEPTIONIST'), ('PATIENT', 'PATIENT'), ('MR', 'MR')], default='PATIENT', max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_data', models.JSONField(blank=True, default=dict, null=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical custom user',
                'verbose_name_plural': 'historical custom users',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('doc_type', models.CharField(blank=True, choices=[('PRESCIPTION', 'PRESCIPTION'), ('TSET', 'TEST')], default='PRESCIPTION', max_length=255, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=ClinicApp.models.get_user_document_filepath)),
                ('disease', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_data', models.JSONField(blank=True, default=list, null=True)),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_uploaded_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.CharField(default=ClinicApp.models.generate_appointment_id, max_length=10)),
                ('appointment_date', models.DateField(blank=True, null=True)),
                ('appointment_time', models.CharField(blank=True, max_length=10, null=True)),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

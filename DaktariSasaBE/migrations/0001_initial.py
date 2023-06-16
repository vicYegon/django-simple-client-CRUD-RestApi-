# Generated by Django 4.2 on 2023-04-27 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('specialty', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('phoneNumber', models.IntegerField()),
                ('age', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField()),
                ('appointmentDate', models.DateField(auto_now_add=True)),
                ('message', models.TextField(null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DaktariSasaBE.departments')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DaktariSasaBE.doctors')),
            ],
            options={
                'verbose_name_plural': 'Appointments',
            },
        ),
    ]

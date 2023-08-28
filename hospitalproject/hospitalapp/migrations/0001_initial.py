# Generated by Django 4.2.1 on 2023-08-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('nid', models.IntegerField()),
                ('area', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chattogram', 'Chattogram'), (' Khulna', ' Khulna'), ('Barishal', 'Barishal'), ('Rajshahi', 'Rajshahi'), ('Sylhet', 'Sylhet'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh')], max_length=200)),
                ('special', models.CharField(choices=[('Nerulogy medicine', 'Nerulogy medicine'), ('Diabetology', 'Diabetology'), ('Chest medicine', 'Chest medicine'), ('Gastroenterologist medicine', 'Gastroenterologist medicine'), ('Nerulogy Surgery', 'Nerulogy Surgery'), ('Cancer Specialist', 'Cancer Specialist')], max_length=200)),
                ('daywork', models.CharField(choices=[('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=200)),
            ],
            options={
                'verbose_name': 'DoctorDetails',
                'verbose_name_plural': 'DoctorDetails',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=200)),
                ('patient_category', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50)),
                ('details', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patient',
            },
        ),
    ]

# Generated by Django 3.1 on 2020-08-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegularPatients',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(blank=True, max_length=64, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(blank=True, max_length=64, null=True)),
                ('occupation', models.CharField(blank=True, max_length=250, null=True)),
                ('regularMedicines', models.TextField(blank=True, null=True)),
                ('repeat_schedule', models.IntegerField(blank=True, null=True)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
                ('time_now', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 3.1 on 2020-09-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0012_auto_20200923_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qr_code',
            field=models.URLField(blank=True, null=True),
        ),
    ]

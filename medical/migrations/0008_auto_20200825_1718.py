# Generated by Django 3.1 on 2020-08-25 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0007_auto_20200825_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsappcustomer',
            name='mobile',
            field=models.CharField(default='Male', max_length=64),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studiosite', '0003_auto_20210628_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='Enquiry',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Feedback',
            field=models.TextField(max_length=1000),
        ),
    ]

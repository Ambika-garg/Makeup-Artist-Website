# Generated by Django 3.2.4 on 2021-07-04 07:48

from django.db import migrations
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('studiosite', '0005_auto_20210629_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='thumb',
            field=imagekit.models.fields.ProcessedImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]

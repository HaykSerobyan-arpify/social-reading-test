# Generated by Django 3.2.10 on 2022-05-18 08:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_user_profile_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_background',
            field=models.ImageField(blank=True, default='profile_default_background.jpeg', null=True, upload_to='profile_backgrounds', validators=[django.core.validators.validate_image_file_extension, django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])]),
        ),
    ]

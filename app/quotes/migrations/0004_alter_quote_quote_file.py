# Generated by Django 3.2.10 on 2022-05-24 13:49
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('quotes', '0003_auto_20220524_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_file',
            field=models.ImageField(upload_to='upload',
                                    validators=[django.core.validators.validate_image_file_extension,
                                                django.core.validators.FileExtensionValidator(
                                                    allowed_extensions=['jpeg', 'png', 'jpg'])], verbose_name='Quote'),
        ),
    ]

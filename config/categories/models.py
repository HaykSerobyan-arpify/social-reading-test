from django.core.validators import MinLengthValidator
from django.db import models
from rest_framework.exceptions import ValidationError
from config.validators import CharValidator
import uuid


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField('category', max_length=15,
                            validators=[MinLengthValidator(limit_value=2, message=None), ], unique=True)

    # add unique category and ignore case
    def save(self, *args, **kwargs):
        if Category.objects.filter(name__iexact=self.name).first():
            raise ValidationError("Invalid code - this code already exists.")
        else:
            self.name = str(self.name).capitalize()
            super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

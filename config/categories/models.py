from django.core.validators import MinLengthValidator
from django.db import models
import uuid

from rest_framework.exceptions import ValidationError


def CharValidator(value):
    if not value.isalpha():
        raise ValidationError(detail='All the characters must be alphabet letters')


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField('category', max_length=15,
                            validators=[MinLengthValidator(limit_value=2, message=None),
                                        CharValidator])

    def __str__(self):
        return self.name

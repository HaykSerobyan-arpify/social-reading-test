from django.core.validators import MinLengthValidator
from django.db import models
from config.validators import CharValidator
import uuid


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

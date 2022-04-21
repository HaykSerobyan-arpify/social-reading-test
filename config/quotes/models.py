import uuid

from django.core.validators import MinLengthValidator, validate_image_file_extension, FileExtensionValidator
from django.db import models
from config.validators import CharValidator


class Quote(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    book_author = models.CharField('Author', max_length=15,
                                   validators=[MinLengthValidator(limit_value=2, message=None),
                                               CharValidator])
    book_title = models.CharField('Title', max_length=15,
                                  validators=[MinLengthValidator(limit_value=2, message=None),
                                              CharValidator])

    book_category = models.CharField('Category', max_length=15,
                                     validators=[MinLengthValidator(limit_value=2, message=None),
                                                 CharValidator])

    quote_file = models.ImageField('Quote', upload_to='',
                                   validators=[validate_image_file_extension,
                                               FileExtensionValidator(allowed_extensions=['jpeg', 'png'])])

    def __str__(self):
        return f'Author: {self.book_author}\n' \
               f'Title: {self.book_title}\n' \
               f'Category: {self.book_category}\n'

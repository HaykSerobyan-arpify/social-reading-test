import uuid
from django.core.validators import MinLengthValidator, validate_image_file_extension, FileExtensionValidator
from django.db import models
from config.validators import CharValidator
from register.models import User


class Quote(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE, verbose_name='Quote author')

    book_author = models.CharField('Book author', max_length=20,
                                   validators=[MinLengthValidator(limit_value=2, message=None), ])

    quote_title = models.CharField('Quote Title', max_length=20,
                                   validators=[MinLengthValidator(limit_value=2, message=None), ])

    book_category = models.CharField('Category', max_length=20,
                                     validators=[MinLengthValidator(limit_value=2, message=None), ])

    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    quote_file = models.ImageField('Quote', upload_to='upload',
                                   validators=[validate_image_file_extension,
                                               FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                   height_field='height',
                                   width_field='width'
                                   )

    quote_text = models.TextField('Quote text', blank=True, null=True)

    text_background = models.ImageField('Quote text background', upload_to='upload',
                                        validators=[validate_image_file_extension,
                                                    FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                        null=True, blank=True)

    save_users = models.ManyToManyField(User, blank=True)

    date_posted = models.DateTimeField(auto_now_add=True)

    likes_by_user = models.ManyToManyField(User, related_name='quote_likes', blank=True)

    def get_comments(self):
        return self.comments.filter(parent=None)

    def total_likes(self):
        return self.likes_by_user.count()

    def __str__(self):
        return f'Author: {self.book_author} | ' \
               f'Title: {self.quote_title} | ' \
               f'Category: {self.book_category} | ' \
               f'User: {self.author}'




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

    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    book_author = models.CharField('Author', max_length=20,
                                   validators=[MinLengthValidator(limit_value=2, message=None), ])
    book_title = models.CharField('Title', max_length=20,
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

    quote_text = models.TextField('Quote text', null=True)

    text_background = models.ImageField('Quote text background', upload_to='upload',
                                        validators=[validate_image_file_extension,
                                                    FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                        null=True)

    # save_users = models.ManyToManyField(User, related_name='save', blank=True)

    date_posted = models.DateTimeField(auto_now_add=True)

    # likes = models.ManyToManyField(User, related_name='quote_likes', blank=True)

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'Author: {self.book_author} | ' \
               f'Title: {self.book_title} | ' \
               f'Category: {self.book_category} | ' \
               f'User: {self.author}'


class Comment(models.Model):
    post = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)

    def __str__(self):
        return self.body

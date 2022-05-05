import uuid
#from updown.fields import RatingField
from django.core.validators import MinLengthValidator, validate_image_file_extension, FileExtensionValidator
from django.db import models
from django.urls import reverse
from config.validators import CharValidator
from register.models import User


class Quote(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    # user_email = models.EmailField('Email', max_length=20, blank=True, help_text='May be blank for tests')
    author = models.ForeignKey(User, related_name='author', on_delete=models.SET_NULL, null=True)

    book_author = models.CharField('Author', max_length=20,
                                   validators=[MinLengthValidator(limit_value=2, message=None),
                                               CharValidator])
    book_title = models.CharField('Title', max_length=20,
                                  validators=[MinLengthValidator(limit_value=2, message=None),
                                              CharValidator])

    book_category = models.CharField('Category', max_length=20,
                                     validators=[MinLengthValidator(limit_value=2, message=None),
                                                 CharValidator])

    quote_file = models.ImageField('Quote', upload_to='upload',
                                   validators=[validate_image_file_extension,
                                               FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])])

    date_posted = models.DateTimeField(auto_now_add=True)

    # rating = RatingField(can_change_vote=True)

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)

    def __str__(self):
        return f'Author: {self.book_author}\n' \
               f'Title: {self.book_title}\n' \
               f'Category: {self.book_category}\n'


class Comment(models.Model):
    post = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name="comments")
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
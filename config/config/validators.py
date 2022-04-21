from rest_framework.exceptions import ValidationError


def CharValidator(value):
    if not value.isalpha():
        raise ValidationError(detail='All the characters must be alphabet letters')
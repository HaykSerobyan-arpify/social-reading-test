from rest_framework.exceptions import ValidationError


def CharValidator(value):
    for el in value.split():
        if '-' in el:
            if not el.replace('-', '').isalpha():
                raise ValidationError(detail='All the characters must be alphabet letters or -')
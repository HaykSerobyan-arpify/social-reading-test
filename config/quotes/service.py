from django_filters import rest_framework as filters
from quotes.models import Quote
import pytesseract
from PIL import Image


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_text_from_picture(image_file):

    image = Image.open(image_file)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config, lang='hye+eng+rus')
    return text


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class QuoteFilter(filters.FilterSet):
    author_id = CharFilterInFilter(field_name='author', lookup_expr='in')
    save = CharFilterInFilter(field_name='save_users', lookup_expr='in')
    category = CharFilterInFilter(field_name='book_category', lookup_expr='in')

    class META:
        model = Quote
        fields = ('author', 'book_category', 'save_users')


from django_filters import rest_framework as filters
from quotes.models import Quote


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class QuoteFilter(filters.FilterSet):
    email = CharFilterInFilter(field_name='user_email', lookup_expr='in')
    category = CharFilterInFilter(field_name='book_category', lookup_expr='in')

    class META:
        model = Quote
        fields = ('user_email', 'book_category', )


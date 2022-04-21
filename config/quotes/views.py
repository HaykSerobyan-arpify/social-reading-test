from rest_framework import serializers
from rest_framework import viewsets
from quotes.models import Quote
from categories.models import Category


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('book_author', 'book_title', 'book_category', 'quote_file')


class QuotesViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()

    def get_success_headers(self, data):
        Category.objects.create(name=data['book_category'])

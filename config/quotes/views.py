from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from quotes.models import Quote
from categories.models import Category
import pymongo
from config.settings import MONGO_URI
from django_filters.rest_framework import DjangoFilterBackend
from quotes.service import get_client_ip, QuoteFilter
from config.settings import DATETIME_FORMAT
from register.views import UserSerializer


def coming_soon(request):
    return render(request, 'quotes/coming_soon.html')


class QuoteSerializer(serializers.ModelSerializer):
    date_posted = serializers.DateTimeField(read_only=True, format=DATETIME_FORMAT, input_formats=None)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Quote
        fields = ('id', 'date_posted', 'likes', 'height',
                  'width ', 'book_author', 'book_title',
                  'book_category', 'quote_file', 'author')


class QuotesViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = QuoteFilter

    def get_success_headers(self, data):
        client = pymongo.MongoClient(MONGO_URI)
        db = client.social_reading_db
        category = data['book_category'].capitalize()
        if db.categories_category.find_one({"name": category}) is None:
            Category.objects.create(name=category)
        print(self.request.user)

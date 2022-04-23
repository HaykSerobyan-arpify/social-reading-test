from rest_framework import serializers
from rest_framework import viewsets
import pymongo

from quotes.models import Quote
from categories.models import Category


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('book_author', 'book_title', 'book_category', 'quote_file')


class QuotesViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
"""
    def get_success_headers(self, data):
        client = pymongo.MongoClient()
        db = client.social_reading_db
        category = data['book_category'].capitalize()
        print(category)
        if db.categories_category.find_one({"name": category}) is None:
            Category.objects.create(name=category)
        print(self.request.user)
"""
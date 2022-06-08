import json
import pprint

import pymongo
from rest_framework import serializers, permissions
from rest_framework import viewsets

from config.settings import MONGO_URI
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'category', 'publisher', 'publish_date', 'sentences',)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_update(self, serializer):
        client = pymongo.MongoClient(MONGO_URI)
        db = client.social_reading_db
        content = db.library_book.find_one({"author": 'sadasd'}).get('content')

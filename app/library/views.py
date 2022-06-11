import pymongo
from rest_framework import serializers, permissions
from rest_framework import viewsets
from app.settings import MONGO_URI
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'category', 'publisher', 'publish_date',)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_update(self, serializer):
        client = pymongo.MongoClient(MONGO_URI)
        db = client.social_reading_db

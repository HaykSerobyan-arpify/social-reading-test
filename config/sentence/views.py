from rest_framework import serializers, permissions
from rest_framework import viewsets
from .models import Sentence


class SentenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sentence
        fields = ('book', 'index_name', 'text')


class SentenceViewSet(viewsets.ModelViewSet):
    serializer_class = SentenceSerializer
    queryset = Sentence.objects.all()


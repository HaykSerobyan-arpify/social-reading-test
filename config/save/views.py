from rest_framework import serializers, permissions
from rest_framework import viewsets

from register.views import UserFieldSerializer
from .models import Save


class SaveSerializer(serializers.ModelSerializer):
    user = UserFieldSerializer(read_only=True)

    class Meta:
        model = Save
        fields = ('id', 'quote', 'user')


class SaveViewSet(viewsets.ModelViewSet):
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

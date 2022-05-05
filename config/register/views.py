from rest_framework import serializers, permissions
from rest_framework import viewsets
from config.settings import DATETIME_FORMAT
from quotes.models import Quote
from .models import User


class UserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True, format=DATETIME_FORMAT, input_formats=None)
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'avatar', 'created')


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Quote.objects.all()
    # permission_classes = (permissions.IsAdminUser,)

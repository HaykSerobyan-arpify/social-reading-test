from django.forms.models import model_to_dict
from rest_framework import serializers, permissions
from rest_framework import viewsets
from config.settings import DATETIME_FORMAT
from .models import User


class UserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True, format=DATETIME_FORMAT, input_formats=None)
    updated = serializers.DateTimeField(read_only=True, format=DATETIME_FORMAT, input_formats=None)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'avatar', 'created',
                  'updated', 'avatar_google', 'avatar_facebook', 'profile_background')
        # read_only_fields = ['avatar_google', 'avatar_facebook', 'profile_background',]


class UserFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        fields = ('id', 'first_name', 'last_name', 'avatar', )


class SaveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        fields = ('id', )


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = (permissions.IsAdminUser,)

from django.contrib.auth import authenticate
from django.core import serializers

from register.models import User
from register.views import UserSerializer
import os
import random
from rest_framework.exceptions import AuthenticationFailed


def generate_username(name):
    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, first_name, last_name, avatar):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:

            registered_user = authenticate(
                email=email, password=os.environ.get('SOCIAL_SECRET'))

            return User.objects.get(email=email).tokens()

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'avatar_google': avatar,
            'password': os.environ.get('SOCIAL_SECRET')}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.is_active = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password=os.environ.get('SOCIAL_SECRET'))
        # print('----------', new_user)
        return user.tokens()

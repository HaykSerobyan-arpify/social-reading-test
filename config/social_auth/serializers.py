from rest_framework import serializers

from config.settings import GOOGLE_CLIENT_ID
from . import google, facebook
from .register import register_social_user
from rest_framework.exceptions import AuthenticationFailed


class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = facebook.Facebook.validate(auth_token)

        try:
            user_id = user_data['id']
            email = user_data['email']
            first_name = user_data['first_name']
            last_name = user_data['last_name']
            avatar = user_data['picture']['data']['url']
            provider = 'facebook'

            return register_social_user(
                provider=provider,
                user_id=user_id,
                email=email,
                first_name=first_name,
                last_name=last_name,
                avatar=avatar,
            )
        except Exception as identifier:
            raise serializers.ValidationError('The token  is invalid or expired. Please login again.')


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']

        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        if user_data['aud'] != GOOGLE_CLIENT_ID:
            raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        first_name = user_data['given_name']
        last_name = user_data['family_name']
        avatar_google = user_data['picture']

        provider = 'google'
        a = {'iss': 'accounts.google.com',
             'azp': '157706975933-5mp07f2obqtjbrtbf3amqvts8s7q8puf.apps.googleusercontent.com',
             'aud': '157706975933-5mp07f2obqtjbrtbf3amqvts8s7q8puf.apps.googleusercontent.com',
             'sub': '117331089545997807598',
             'email': 'manchess20@gmail.com',
             'email_verified': True,
             'at_hash': 'Sld138ew7Wt8B7HJd5ERoA',
             'name': 'Tigran Aghajanyan',
             'picture': 'https://lh3.googleusercontent.com/a-/AOh14GiM1p5t-DQStkpwzTWMN5QwyoRrZk-MIF-uW3cfVA=s96-c',
             'given_name': 'Tigran',
             'family_name': 'Aghajanyan',
             'locale': 'ru',
             'iat': 1652278589,
             'exp': 1652282189,
             'jti': 'ca9a5a4b1841c6761721345fca31e9bae1808fd4'}

        return register_social_user(
            provider=provider, user_id=user_id,
            email=email, first_name=first_name,
            last_name=last_name, avatar=avatar_google)

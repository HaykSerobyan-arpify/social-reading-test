from django.core.exceptions import FieldError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from pymongo.errors import BulkWriteError
from rest_framework import serializers, status
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from comments.views import CommentsSerializer
from likes.views import LikeSerializer
from quotes.models import Quote
from categories.models import Category
import pymongo
from config.settings import MONGO_URI
from django_filters.rest_framework import DjangoFilterBackend
from quotes.service import get_client_ip, QuoteFilter, get_text_from_picture
from config.settings import DATETIME_FORMAT
from django.views.generic.base import View
from django.contrib.auth.models import AnonymousUser
from register.views import UserSerializer


def coming_soon(request):
    return render(request, 'quotes/coming_soon.html')


def like_quote(request):
    quote = get_object_or_404(Quote, id=request.POST.get('quote_id'))
    if quote.likes.filter(id=request.user.id).exists():
        pass
    else:
        quote.likes.add(request.user)
    return HttpResponseRedirect(reverse('coming_soon'))


class QuoteSerializer(serializers.ModelSerializer):
    date_posted = serializers.DateTimeField(read_only=True, format=DATETIME_FORMAT, input_formats=None)
    author = UserSerializer(read_only=True)
    likes = LikeSerializer(many=True)
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Quote
        fields = ('id', 'author', 'date_posted',
                  'book_author', 'quote_title', 'book_category',
                  'quote_file', 'quote_text', 'styles',
                  'text_background', 'likes',
                  'save_users', 'comments', 'published', 'is_active')


class QuotesViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all().order_by('-date_posted')
    filter_backends = (DjangoFilterBackend,)
    filterset_class = QuoteFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):

        # text recognition
        quote_text = get_text_from_picture(self.request.data.get('quote_file'))
        try:
            if isinstance(self.request.user, AnonymousUser):
                serializer.save(author=None, quote_text=quote_text,
                                quote_title='Book title(Recognized by Python)',
                                book_author='Book author(Recognized by Python)')
            else:
                serializer.save(author=self.request.user, quote_text=quote_text,
                                quote_title='Book title(Recognized by Python)',
                                book_author='Book author(Recognized by Python)')
        except ValueError:
            raise FieldError("User must be authorised")

    def get_success_headers(self, data):
        client = pymongo.MongoClient(MONGO_URI)
        db = client.social_reading_db
        category = data['book_category'].capitalize()
        user = self.request.user
        if db.categories_category.find_one({"name": category}) is None:
            new_category = Category.objects.create(name=category)
            new_category.users.add(user)
        else:
            cat = Category.objects.get(name=category)
            try:
                cat.users.add(self.request.user)
            except BulkWriteError:
                # if user exists in category users
                pass
            except Exception:
                # if user exists in category users
                pass


class PublishQuotesViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.filter(published=True)


class QuotesViewHTML(View):

    def get(self, request):
        quotes = Quote.objects.all()
        return render(request, 'quotes/quote_list.html', {'quote_list': quotes})

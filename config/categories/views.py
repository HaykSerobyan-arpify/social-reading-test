from rest_framework import serializers
from rest_framework import viewsets
from .models import Category
from ipware import get_client_ip


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_success_headers(self, data):
        if self.request.method == "POST":
            # We get ip here
            client_ip, is_routable = get_client_ip(self.request)

            print(client_ip)
            print(is_routable)
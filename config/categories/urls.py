from django.urls import include, path
from rest_framework_nested import routers

from .views import CategoriesViewSet

router = routers.SimpleRouter()
router.register('', CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
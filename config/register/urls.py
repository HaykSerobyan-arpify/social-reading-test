from django.urls import include, path
from rest_framework import routers
from .views import UsersViewSet

router = routers.SimpleRouter()
router.register('', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
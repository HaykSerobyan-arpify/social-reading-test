from django.urls import path
from rest_framework import routers
from .views import QuotesViewSet, QuotesViewHTML

router = routers.SimpleRouter()
router.register('', QuotesViewSet)

urlpatterns = router.urls
urlpatterns += [path('view/html/', QuotesViewHTML.as_view())]

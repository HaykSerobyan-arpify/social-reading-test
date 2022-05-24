from django.urls import path
from rest_framework import routers
from .views import QuotesViewSet, QuotesViewHTML, PublishQuotesViewSet

router = routers.SimpleRouter()
router.register('', QuotesViewSet)
router.register('published', PublishQuotesViewSet)

urlpatterns = router.urls
urlpatterns += [path('view/html/', QuotesViewHTML.as_view())]

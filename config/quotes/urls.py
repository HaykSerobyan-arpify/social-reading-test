from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
import quotes.views
from .views import QuotesViewSet, QuotesViewHTML

router = routers.SimpleRouter()
router.register('', QuotesViewSet)

urlpatterns = router.urls
urlpatterns += [path('view/html/', QuotesViewHTML.as_view())]

# urlpatterns += format_suffix_patterns([
#     path("quote/", quotes.views.QuotesViewSet.as_view({'get': 'list'})),
#     # path("quote/<int:pk>/", quotes.views.QuotesViewSet.as_view({'get': 'retrieve'})),
#     # path("comment/", quotes.views.CommentCreateViewSet.as_view({'post': 'create'})),
# ])

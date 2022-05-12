"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from config.settings import MEDIA_ROOT, STATIC_ROOT, STATIC_URL
from django.views.static import serve
from quotes.views import coming_soon, like_quote

# DRF YASG
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

schema_view = get_schema_view(
    openapi.Info(
        title="Social Reading App Documentation",
        default_version="v1",
        description="REST implementation of Django authentication system. djoser library provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation. It works with custom user model.",
        contact=openapi.Contact(email="haykserobyan@arpify.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', coming_soon, name='coming_soon'),
    path('social_auth/', include(('social_auth.urls', 'social_auth'),
                                 namespace="social_auth")),
    path('admin/', admin.site.urls),
    re_path(r'like/<uuid:id>', like_quote, name='like_quote'),
    path('categories/', include('categories.urls')),
    path('quotes/', include('quotes.urls')),
    path('register/', include('register.urls')),
    path('auth/', include("djoser.urls")),
    path('auth/djoser/', include('djoser.urls.jwt')),
    # re_path(r'^auth/', include('djoser.social.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('oauth/', include('social_django.urls', namespace='social')),
    re_path(
        r"docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT, }), ]

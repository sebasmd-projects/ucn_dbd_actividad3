from django.urls import include, path

from .api import urls as api_urls

urlpatterns = [
    path('api/users/', include(api_urls.urlpatterns)),
]

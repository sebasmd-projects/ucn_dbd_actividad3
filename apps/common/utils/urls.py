from django.urls import include, re_path

from .api import urls as api_urls

urlpatterns = [
    re_path(r'^api/logs/v1/', include(api_urls.log_urlpattern)),
    re_path(r'^api/auth/v1/', include(api_urls.urlpatterns)),
]

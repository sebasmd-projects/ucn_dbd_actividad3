from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

custom_apps = settings.CUSTOM_APPS

apps_urls = [path('', include(f'{app}.urls')) for app in custom_apps]

apps_urls_i18n = i18n_patterns(
    prefix_default_language=False,
    # path(
    #     '',
    #     include('apps.common.utils.urls_i18n')
    # )
)

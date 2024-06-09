from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .urls_custom import apps_urls, apps_urls_i18n

admin_url = settings.ADMIN_URL
utils_path = settings.UTILS_PATH
current_domain = settings.DOMAIN


handler400 = f'{utils_path}.views.handler400'

handler403 = f'{utils_path}.views.handler403'

handler404 = f'{utils_path}.views.handler404'

handler500 = f'{utils_path}.views.handler500'


# YASG schema view
schema_view = get_schema_view(
    openapi.Info(
        title='Backend Endpoints',
        default_version='v1.0.0',
        description=_(
            'Documentación de la API y representación de los endpoints'),
        terms_of_service='',
        contact=openapi.Contact(email=settings.YASG_EMAIL),
        license=openapi.License(name=settings.YASG_TERMS_OF_SERVICE),
    ),
    public=False,
)

# Admin and debug urls
urlpatterns_general = [
    path(
        admin_url,
        admin.site.urls
    ),
    re_path(
        r"^sitemap.xml",
        sitemap,
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path(
        '__debug__/',
        include('debug_toolbar.urls')
    ),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view()
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view()
    ),
]

# Django yet another swagger generator urls
urlpatterns_general += [
    re_path(
        r'^api/docs/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
    ),
    re_path(
        r'^api/redocs/',
        schema_view.with_ui(
            'redoc',
            cache_timeout=0
        ),
        name='schema-redoc'
    ),
    re_path(
        r'^api/docs/<format>/',
        schema_view.without_ui(
            cache_timeout=0
        ),
        name='schema-json-yaml'
    ),
]


# Rosetta (Translation progress)
urlpatterns_general += [
    re_path(
        r'^rosetta/',
        include('rosetta.urls')
    )
]

# Static files urls
urlpatterns_general += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)

# Media files urls
urlpatterns_general += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)


urlpatterns = [
    path(
        '',
        include(apps_urls)
    )
]

urlpatterns += apps_urls_i18n + urlpatterns_general
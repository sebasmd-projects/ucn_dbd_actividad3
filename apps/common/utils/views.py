from django.conf import settings
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenBlacklistView,
                                            TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .api import (TokenBlacklistResponseSerializer,
                  TokenObtainPairResponseSerializer,
                  TokenRefreshResponseSerializer,
                  TokenVerifyResponseSerializer)
from .backend import EmailOrUsernameModelBackend

try:
    template_name = settings.ERROR_TEMPLATE
except:
    template_name = 'errors_template.html'


def handler400(request, exception, *args, **argv):
    status = 400
    return render(
        request,
        template_name,
        status=status,
        context={
            'exception': str(exception),
            'title': _('Error 400'),
            'error': _('Solicitud Incorrecta'),
            'status': status,
            'error_favicon': ''
        }
    )


def handler403(request, exception, *args, **argv):
    status = 403
    return render(
        request,
        template_name,
        status=status,
        context={
            'exception': str(exception),
            'title': _('Error 403'),
            'error': _('Solicitud Prohibida'),
            'status': status,
            'error_favicon': ''
        }
    )


def handler404(request, exception, *args, **argv):
    status = 404
    return render(
        request,
        template_name,
        status=status,
        context={
            'exception': str(exception),
            'title': _('Error 404'),
            'error': _('Página no encontrada'),
            'status': status,
            'error_favicon': ''
        }
    )


def handler500(request, *args, **argv):
    status = 500
    return render(
        request,
        template_name,
        status=500,
        context={
            'title': _('Error 500'),
            'error': _('Error del Servidor'),
            'status': status,
            'error_favicon': ''
        }
    )


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        username_or_email = request.data.get('username')
        backend = EmailOrUsernameModelBackend()
        user = backend.authenticate(
            request,
            username=username_or_email,
            password=request.data.get(
                'password'
            )
        )

        if user:
            response.data['user_id'] = user.id

        return response


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenVerifyView(TokenVerifyView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenVerifyResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            response.data['detail'] = 'Token is valid'
            response.data['code'] = 'token_is_valid'

        return response


class DecoratedTokenBlacklistView(TokenBlacklistView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenBlacklistResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

from django_filters.rest_framework import CharFilter, DateTimeFilter, FilterSet

from ..models import UserModel


class UserModelFilter(FilterSet):
    username = CharFilter(
        field_name='username',
        lookup_expr='icontains'
    )
    first_name = CharFilter(
        field_name='first_name',
        lookup_expr='icontains'
    )
    last_name = CharFilter(
        field_name='last_name',
        lookup_expr='icontains'
    )
    email = CharFilter(
        field_name='email',
        lookup_expr='exact'
    )
    created = DateTimeFilter(
        field_name='created',
        lookup_expr='range'
    )
    updated = DateTimeFilter(
        field_name='updated',
        lookup_expr='range'
    )

    class Meta:
        model = UserModel
        fields = [
            'username',
            'first_name',
            'last_name',
            'is_active',
            'created',
            'updated',
            'email'
        ]

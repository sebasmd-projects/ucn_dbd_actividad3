from rest_framework.serializers import ModelSerializer

from ..models import UserModel


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class UserModelSerializerGET(ModelSerializer):
    class Meta:
        model = UserModel
        exclude = [
            'password',
            'is_superuser',
            'is_staff',
            'user_permissions',
            'default_order',
            'groups',
        ]


class UserModelSerializerPOST_PUT_PATCH(ModelSerializer):
    class Meta:
        model = UserModel
        exclude = [
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'user_permissions',
            'created',
            'updated',
            'default_order',
            'groups',
        ]

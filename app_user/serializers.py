from django.contrib.auth.models import User
from rest_framework import serializers, validators

from app_user.models import AppUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ("username", "password", "email", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        AppUser.objects.all(), f"A user with that Email already exists."
                    )
                ],
            },
        }

    def create(self, validated_data):
        user = AppUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )
        return user

class AppUserSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source = 'user.username')
    class Meta:
        model = AppUser
        fields = ['user', 'user_type', 'gender', 'mobile', 'address', 'city',  'pincode']
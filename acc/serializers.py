from rest_framework import serializers
# from models import CustomUser
from .services import UserDataClass

class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

    # class Meta:
    #     model = CustomUser
    #     fields = "__all__"

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return UserDataClass(**data)

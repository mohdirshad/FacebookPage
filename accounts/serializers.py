from rest_framework import serializers

from .models import User


class FbRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    image_url = serializers.URLField(required=False)
    facebook_id = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('name','email', 'image_url', 'facebook_id', )


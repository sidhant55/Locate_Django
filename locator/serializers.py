from rest_framework import serializers
from .models import Locator


class LocatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locator
        fields = "__all__"

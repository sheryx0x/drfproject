from rest_framework import serializers
from .models import snippet


class snippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = snippet
        fields = '__all__'
from rest_framework import serializers
from .models import snippet


class snippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
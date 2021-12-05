from rest_framework import serializers

from .models import TextClassification


class TextClassificationSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=255)
    description = serializers.CharField()
    flag = serializers.BooleanField()
    status = serializers.CharField(max_length=255)
    tag = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return TextClassification.objects.create(**validated_data)

    class Meta:
        model = TextClassification
        fields = ('url', 'description', 'flag', 'status', 'tag')

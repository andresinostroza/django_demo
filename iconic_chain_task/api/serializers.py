from rest_framework import serializers

from iconic_chain_task.api.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'filename', 'organization', 'user', 'created_at']

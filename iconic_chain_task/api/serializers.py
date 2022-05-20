from rest_framework import serializers

from iconic_chain_task.api.models import IconicFile, IconicFileDownloadLog, Organization, User


class IconicFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconicFile
        fields = ['id', 'file', 'organization', 'user', 'created_at']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'organization']


class IconicFileDownloadLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconicFileDownloadLog
        fields = ['id', 'file', 'organization', 'user', 'created_at']

from rest_framework import serializers

from iconic_chain_task.api.models import (
    IconicFile,
    IconicFileDownloadLog,
    Organization,
    User,
)


class IconicFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconicFile
        fields = ["id", "file", "organization", "user", "created_at"]

    def get_downloads(self, fileId):
        return IconicFileDownloadLog.objects.filter(file__id=fileId).count()

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "filename": instance.filename,
            "created_at": instance.created_at,
            "downloads": self.get_downloads(instance.id),
        }


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "name"]

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "filename": instance.name,
            "downloads": IconicFileDownloadLog.objects.filter(
                organization__id=instance.id
            ).count(),
        }


class UserSerializer(serializers.ModelSerializer):
    downloads = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "email", "organization", "downloads"]

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "email": instance.email,
            "organization_id": instance.organization.id,
            "downloads": IconicFileDownloadLog.objects.filter(
                user__id=instance.id
            ).count(),
        }


class IconicFileDownloadLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconicFileDownloadLog
        fields = ["id", "file", "organization", "user", "created_at"]

    def to_representation(self, instance):
        return {
            "file_id": instance.file.id,
            "downloaded_at": instance.created_at,
        }

from django.db import models

from .organization import Organization
from .user import User


class IconicFile(models.Model):
    file = models.FileField(null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    @property
    def filename(self):
        return self.file.name.split("/")[-1]

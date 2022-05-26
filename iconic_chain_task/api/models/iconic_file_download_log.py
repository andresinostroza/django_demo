from django.db import models

from .organization import Organization
from .iconic_file import IconicFile
from .user import User


class IconicFileDownloadLog(models.Model):
    file = models.ForeignKey(IconicFile, on_delete=models.PROTECT)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} has been downloaded by {self.user.email}"

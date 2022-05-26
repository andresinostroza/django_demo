from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from django.test.testcases import SerializeMixin

from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse

from iconic_chain_task.api.models.organization import Organization
from iconic_chain_task.api.models.user import User


class initDBTestCaseMixin(SerializeMixin, object):
    lockfile = __file__

    def setUp(self):
        self.organization = Organization.objects.create(name="test")
        self.admin_user = User.objects.create_superuser(
            email="admin@admin.com", password="password"
        )


class LoginUserTestCaseMixin(initDBTestCaseMixin, SerializeMixin):
    lockfile = __file__

    def setUp(self):
        super(LoginUserTestCaseMixin, self).setUp()
        token = Token.objects.create(user=self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(token))


class UploadFileTestCaseMixin(LoginUserTestCaseMixin, SerializeMixin):
    lockfile = __file__

    def setUp(self):
        super(UploadFileTestCaseMixin, self).setUp()
        upload_file_url = reverse("upload_file")
        data = File(open("/code/README.md", "rb"))
        upload_file = SimpleUploadedFile("README.md", data.read())
        response = self.client.post(
            upload_file_url, {"file": upload_file}, format="multipart"
        )
        self.uploaded_file = response.data

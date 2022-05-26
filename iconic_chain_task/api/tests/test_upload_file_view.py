from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File


from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from iconic_chain_task.api.tests.mixins import LoginUserTestCaseMixin


class UploadFileViewsSetTest(LoginUserTestCaseMixin, APITestCase):
    def test_post_file(self):
        upload_file_url = reverse("upload_file")
        data = File(open("/code/README.md", "rb"))
        upload_file = SimpleUploadedFile("README.md", data.read())
        response = self.client.post(
            upload_file_url, {"file": upload_file}, format="multipart"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_file_wrong_format_post(self):
        upload_file_url = reverse("upload_file")
        data = File(open("/code/README.md", "rb"))
        upload_file = SimpleUploadedFile("README.md", data.read())
        response = self.client.post(
            upload_file_url, {"file": upload_file}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_file_with_no_file(self):
        upload_file_url = reverse("upload_file")
        response = self.client.post(upload_file_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

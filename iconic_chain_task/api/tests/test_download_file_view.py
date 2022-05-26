from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from iconic_chain_task.api.tests.mixins import UploadFileTestCaseMixin


class DownloadFileViewsSetTest(UploadFileTestCaseMixin, APITestCase):
    def test_get_existing_file(self):
        get_file_url = reverse("download_file", args=[self.uploaded_file["id"]])
        response = self.client.get(get_file_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_non_existing_file(self):
        get_file_url = reverse("download_file", args=[self.uploaded_file["id"] + 1])
        response = self.client.get(get_file_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

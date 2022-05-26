from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from iconic_chain_task.api.tests.mixins import UploadFileTestCaseMixin


class DownloadFileViewsSetTest(UploadFileTestCaseMixin, APITestCase):
    def setUp(self):
        super(DownloadFileViewsSetTest, self).setUp()
        get_file_url = reverse("download_file", args=[self.uploaded_file["id"]])
        self.client.get(get_file_url)

    def test_get_users_has_download(self):
        get_user_download_logs_url = reverse(
            "get_user_download_logs", args=[self.admin_user.id]
        )
        response = self.client.get(get_user_download_logs_url)
        self.assertTrue(len(response.data) == 1)

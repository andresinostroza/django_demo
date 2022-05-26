from rest_framework.reverse import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from iconic_chain_task.api.tests.mixins import LoginUserTestCaseMixin


class UserViewsSetTest(LoginUserTestCaseMixin, APITestCase):
    def test_get_users(self):
        get_users_url = reverse("get_users")
        response = self.client.get(get_users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_download_log(self):
        get_user_download_logs_url = reverse(
            "get_user_download_logs", args=[self.admin_user.id]
        )
        response = self.client.get(get_user_download_logs_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_download_log_not_found(self):
        get_user_download_logs_url = reverse(
            "get_user_download_logs", args=[self.admin_user.id + 1]
        )
        response = self.client.get(get_user_download_logs_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_no_user_download_logs_when_app_starts(self):
        get_user_download_logs_url = reverse(
            "get_user_download_logs", args=[self.admin_user.id]
        )
        response = self.client.get(get_user_download_logs_url)
        self.assertEqual(len(response.data), 0)

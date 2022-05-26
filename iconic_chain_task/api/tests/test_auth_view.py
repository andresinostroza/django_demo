from rest_framework.reverse import reverse

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status

from iconic_chain_task.api.models import User
from iconic_chain_task.api.tests.mixins import initDBTestCaseMixin


class AuthViewsSetTest(initDBTestCaseMixin, APITestCase):
    def test_existing_super_user(self):
        admin_user = User.objects.get(email="admin@admin.com")
        self.assertEqual(admin_user.is_superuser, True)

    def test_login_correct_credentials(self):
        login_url = reverse("login")
        login_data = {"username": "admin@admin.com", "password": "password"}
        response = self.client.post(login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_wrong_credentials(self):
        login_url = reverse("login")
        login_data = {"username": "admin@admin.com", "password": "passwords"}
        response = self.client.post(login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_with_token(self):
        logou_url = reverse("logout")
        admin_user = User.objects.get(email="admin@admin.com")
        token = Token.objects.create(user=admin_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(token))
        response = self.client.post(logou_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_with_no_token(self):
        logou_url = reverse("logout")
        response = self.client.post(logou_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

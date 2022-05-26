from rest_framework.reverse import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from iconic_chain_task.api.tests.mixins import LoginUserTestCaseMixin


class OrganizationViewsSetTest(LoginUserTestCaseMixin, APITestCase):
    def test_get_organizations(self):
        get_organizations_url = reverse("get_organizations")
        response = self.client.get(get_organizations_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_at_least_default_organization(self):
        get_organizations_url = reverse("get_organizations")
        response = self.client.get(get_organizations_url)
        self.assertTrue(len(response.data) >= 1)

    def test_get_organization_files(self):
        get_organizations_url = reverse(
            "get_organizations_files", args=[self.organization.id]
        )
        response = self.client.get(get_organizations_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_organization_files_by_default(self):
        get_organizations_url = reverse(
            "get_organizations_files", args=[self.organization.id]
        )
        response = self.client.get(get_organizations_url)
        self.assertEqual(len(response.data), 0)

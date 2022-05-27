from django.test import TestCase

from iconic_chain_task.api.models.organization import Organization


class TestModels(TestCase):
    def test_organization_parse_str_as_org_name(self):
        self.organization = Organization.objects.create(name="test")
        self.assertEqual(str(self.organization), "test")

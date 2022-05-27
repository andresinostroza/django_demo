from django.test import TestCase

from iconic_chain_task.api.models.organization import Organization
from iconic_chain_task.api.models.user import User


class TestModels(TestCase):
    def test_create_super_user_with_no_email(self):
        Organization.objects.create(name="test")
        self.assertRaises(ValueError, User.objects.create_superuser, None, "arg2")

    def test_create_super_user_with_no_password(self):
        Organization.objects.create(name="test")
        self.assertRaises(
            ValueError, User.objects.create_superuser, "admin@admin.com", None
        )

    def test_create_super_user_with_no_org(self):
        self.assertRaises(
            ValueError, User.objects.create_superuser, "admin@admin.com", "arg2"
        )

    def test_create_user_with_specific_org(self):
        organization = Organization.objects.create(name="test")
        user = User.objects.create_user(
            email="admin@admin.com",
            password="password",
            organization_id=organization.id,
        )
        self.assertEqual(organization.id, user.organization.id)

    def test_str_parse_as_email(self):
        Organization.objects.create(name="test")
        user = User.objects.create_user(email="admin@admin.com", password="password")
        self.assertEqual(str(user), user.email)

    def test_user_always_staff(self):
        Organization.objects.create(name="test")
        user = User.objects.create_user(email="admin@admin.com", password="password")
        self.assertTrue(user.is_staff)

    def test_create_user_with_wrong_org_id(self):
        Organization.objects.create(name="test")
        self.assertRaises(
            Organization.DoesNotExist,
            User.objects.create_user,
            "admin@admin.com",
            "arg2",
            5,
        )

from django.test import TestCase
from iconic_chain_task.api.models import User, Organization


class UserTest(TestCase):
    def setUp(self):
        Organization.objects.create(name="test")
        User.objects.create_superuser(email="admin@admin.com", password="password")

    def test_create_super_user(self):
        admin_user = User.objects.get(email="admin@admin.com")
        self.assertEqual(admin_user.is_superuser, True)

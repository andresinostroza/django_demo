from django.test import TestCase

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File

from iconic_chain_task.api.models.iconic_file import IconicFile
from iconic_chain_task.api.tests.mixins import initDBTestCaseMixin


class TestModels(initDBTestCaseMixin, TestCase):
    def test_str_parse_as_filename(self):
        data = File(open("/code/README.md", "rb"))
        simple_file = SimpleUploadedFile("README.md", data.read())
        iconic_file = IconicFile.objects.create(
            file=simple_file, organization=self.organization, user=self.admin_user
        )
        self.assertEqual(str(iconic_file), iconic_file.file.name)

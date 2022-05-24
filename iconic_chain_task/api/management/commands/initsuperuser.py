import os

from django.core.management.base import BaseCommand

from iconic_chain_task.api.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
            password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
            print("Creating account for %s" % (email))
            admin = User.objects.create_superuser(email=email, password=password)
            admin.save()
        else:
            print(
                "Admin accounts can only be initialized when the app get build for first time"
            )

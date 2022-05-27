from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

from .organization import Organization


class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None, organization_id=None):
        if not email:
            raise ValueError("User must have an email address")

        if not password:
            raise ValueError("User must set a password")

        if not organization_id:
            default_organization = Organization.objects.first()
            if not default_organization:
                raise ValueError(
                    "Organizations have not been set, "
                    "please run: python manage.py loaddata "
                    "organization following "
                    "the instructions in the README.md file"
                )
        else:
            # TODO what if I give a bad org id?
            default_organization = Organization.objects.get(id=organization_id)

        email = self.normalize_email(email)
        user = self.model(email=email, organization=default_organization)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create a new superuser profile"""
        user = self.create_user(email, password)
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return True

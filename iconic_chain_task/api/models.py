from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None, organization_id=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        # TODO Refactor to another function, even a class
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
            default_organization = Organization.objects.get(id=organization_id)

        email = self.normalize_email(email)
        user = self.model(email=email, organization=default_organization)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create a new superuser profile"""
        print("Creating root user!")
        user = self.create_user(email, password)
        user.is_superuser = True

        user.save(using=self._db)

        return user


class Organization(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


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


class IconicFile(models.Model):
    file = models.FileField(null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    @property
    def filename(self):
        return self.file.name.split("/")[-1]


class IconicFileDownloadLog(models.Model):
    file = models.ForeignKey(IconicFile, on_delete=models.PROTECT)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} has been downloaded by {self.user.email}"

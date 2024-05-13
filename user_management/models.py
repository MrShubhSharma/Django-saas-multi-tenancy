from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class Organization(models.Model):
    name = models.CharField(max_length=100)
    url = models.SlugField(unique=True, blank=True, null=True)  # URL field using slug

    def save(self, *args, **kwargs):
        # Auto-generate URL using the organization name
        self.url = slugify(self.name)
        super(Organization, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='users', null=True, blank=True)

    def __str__(self):
        return self.username

class OrganizationUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class Role(models.Model):
    name = models.CharField(max_length=50)

class Permission(models.Model):
    name = models.CharField(max_length=100)

class Group(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission)

class GroupRole(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

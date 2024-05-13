from django.contrib import admin
from .models import CustomUser, Organization, Role, Permission, Group, GroupRole, OrganizationUser

admin.site.register(CustomUser)
admin.site.register(Organization)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Group)
admin.site.register(GroupRole)
admin.site.register(OrganizationUser)

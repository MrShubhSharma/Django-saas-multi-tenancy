from rest_framework import viewsets
from .models import CustomUser, Organization, Role, Permission, Group, GroupRole, OrganizationUser
from .serializers import UserSerializer, OrganizationSerializer, RoleSerializer, PermissionSerializer, GroupSerializer, GroupRoleSerializer, OrganizationUserSerializer
from django.shortcuts import render, get_object_or_404

from .models import Organization


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupRoleViewSet(viewsets.ModelViewSet):
    queryset = GroupRole.objects.all()
    serializer_class = GroupRoleSerializer

class OrganizationUserViewSet(viewsets.ModelViewSet):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer



# def organization_template_view(request, organization_id):
#     # Get organization by id
#     organization = Organization.objects.get(pk=organization_id)

#     # Render template with organization name
#     return render(request, 'organization_template.html', {'organization': organization})




def organization_template_view(request, organization_url):
    organization = get_object_or_404(Organization, url=organization_url)
    return render(request, 'user_management/organization_template.html', {'organization': organization})


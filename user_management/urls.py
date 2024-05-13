from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, OrganizationViewSet, RoleViewSet, PermissionViewSet, GroupViewSet, GroupRoleViewSet, OrganizationUserViewSet
from .views import organization_template_view

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'grouproles', GroupRoleViewSet)
router.register(r'organizationusers', OrganizationUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
#     path('organization/<int:organization_id>/', organization_template_view, name='organization_template'),
# ]

    path('<str:organization_url>/', organization_template_view, name='organization_template'),
]
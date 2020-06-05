"""lello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

from users.views import UserViewSet, UserDetailViewSet, TeamViewSet
from boards.views import BoardViewSet, ListViewSet, CardViewSet, LabelViewSet
from checklists.views import ChecklistViewSet, ElementViewSet
from calendars.views import CalendarViewSet, EventViewSet
from notifications.views import NotificationViewSet
from audits.views import AuditViewSet

from init_data import create_initial_data

from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userdetails', UserDetailViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)
router.register(r'labels', LabelViewSet)
router.register(r'checklists', ChecklistViewSet)
router.register(r'elements', ElementViewSet)
router.register(r'calendars', CalendarViewSet)
router.register(r'events', EventViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'audits', AuditViewSet)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^api/token-auth/', obtain_jwt_token),
    url(r'^api/token-refresh/', refresh_jwt_token),
    url(r'^api/token-verify/', verify_jwt_token),
    url(r'^admin/initial-data/', create_initial_data),
    url(r'send/', include('users.urls')),
]

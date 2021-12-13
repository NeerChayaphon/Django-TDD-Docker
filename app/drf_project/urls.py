from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions

from .views import ping





urlpatterns = [
    path("admin/", admin.site.urls),
    path("ping/", ping, name="ping"),
    path("", include("movies.urls")),
]
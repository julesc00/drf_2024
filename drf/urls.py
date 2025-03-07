
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1.0/", include("api.urls")),
]

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authtoken/', include("authtoken.urls")),
    path('user/', include("user.urls")),
]

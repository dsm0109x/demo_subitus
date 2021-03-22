from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from demo.code import code
from demo.code.api import api
from django.urls import include, path


urlpatterns = [
    path("", code.inicio, name="inicio"),
    path("avatar/", code.avatar, name="avatar"),

    # API
    path("api/send-data/", api.send_data, name="API-send-data"),
    path("api/last-user/", api.last_user, name="API-last-user"),

    # otros
    path("root/", admin.site.urls),
]

# Media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
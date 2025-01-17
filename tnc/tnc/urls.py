"""TNC URL Configuration"""

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

from .views import index

urlpatterns = [
    # path("__debug__/", include("debug_toolbar.urls")),
    path("addi/", admin.site.urls),
    path("banking/", include("banking.urls")),
    path("", index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + debug_toolbar_urls()

handler404 = "tnc.views.page_not_found_view"

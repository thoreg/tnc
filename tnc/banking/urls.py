from django.urls import path

from . import views

urlpatterns = [
    path("upload", views.index, name="banking_upload_files"),
    path("", views.index, name="banking_index"),
]

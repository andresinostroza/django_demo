from django.urls import path

from rest_framework.authtoken import views as rest_framework_views

from . import views


urlpatterns = [
    path("login/", rest_framework_views.obtain_auth_token, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("file/", views.post_file, name="upload_file"),
    path("file/<int:file_id>/download", views.get_file, name="download_file"),
    path("user/", views.get_users, name="get_users"),
    path(
        "user/<int:user_id>/download-log",
        views.get_user_downloads,
        name="get_user_download_logs",
    ),
    path("organization/", views.get_organizations, name="get_organizations"),
    path(
        "organization/<int:organization_id>/files",
        views.get_files,
        name="get_organizations_files",
    ),
]

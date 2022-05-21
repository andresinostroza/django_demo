from django.urls import path
from rest_framework.authtoken import views as rest_framework_views

from . import views

urlpatterns = [
    path('login/', rest_framework_views.obtain_auth_token),
    path('logout/', views.user_logout),
    path('file/', views.post_file),
    path('file/<int:file_id>/download', views.get_file),
    path('user/', views.get_users),
    path('user/<int:user_id>/download-log', views.get_user_downloads),
    path('organization/', views.get_organizations),
    path('organization/<int:organization_id>/files', views.get_files),
]

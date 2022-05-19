from django.urls import path
from rest_framework.authtoken import views as rest_framework_views

from . import views

urlpatterns = [
    path('login/', rest_framework_views.obtain_auth_token),
    path('logout/', views.user_logout)
]

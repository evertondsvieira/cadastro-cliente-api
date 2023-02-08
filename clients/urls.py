from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("clients/", views.ClientView.as_view()),
    path("clients/<int:pk>/", views.ClientDetailView.as_view()),
    path("clients/login/", jwt_views.TokenObtainPairView.as_view()),
]
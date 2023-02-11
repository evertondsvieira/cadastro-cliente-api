from django.urls import path
from . import views

urlpatterns = [
    path("users/<int:pk>/contacts/", views.ContactView.as_view()),
]
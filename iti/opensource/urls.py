from django.urls import path
from opensource import views


urlpatterns = [
    path("home/", views.home),
    path("students/<id>/", views.getStudent),
    path("students/", views.getStudents),
]

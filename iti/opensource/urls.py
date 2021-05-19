from django.urls import path
from .views import home, getStudent, getStudents, newStudent, editStudent,deleteStudent


urlpatterns = [
    path("home/", home),
    path("students/<id>/", getStudent),
    path("students/", getStudents),
    path("newstudent/", newStudent),
    path("editstudent/<id>", editStudent),
    path("deletestudent/<id>", deleteStudent),
    
]

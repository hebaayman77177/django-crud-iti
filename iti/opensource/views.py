from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.


def home(request):
    return HttpResponse("<h1>hiiiiiiiiiiiiii</h1>")


def getStudent(request, id):
    st = Student.objects.get(id=id)
    context = {"student": st}
    return render(request, "opensource/student.html", context)


def getStudents(request):
    sts = Student.objects.all()
    context = {"students": sts}
    return render(request, "opensource/allstudents.html", context)

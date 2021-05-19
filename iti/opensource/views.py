from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from .forms import TrackForm, StudentForm

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


def newStudent(request):
    st_form = StudentForm()
    if request.method == "POST":
        st_form = StudentForm(request.POST)
        if st_form.is_valid:
            st_form.save()
            return HttpResponseRedirect("/opensource/students")
    context = {"st_form": st_form}
    return render(request, "opensource/new_student.html", context)




def editStudent(request,id):
    st = Student.objects.get(id=id)
    st_form = StudentForm(instance=st)
    if request.method == "POST":
        st_form = StudentForm(request.POST,instance=st)
        if st_form.is_valid:
            st_form.save()
            return HttpResponseRedirect("/opensource/students")
    context = {"st_form": st_form}
    return render(request, "opensource/new_student.html", context)




def deleteStudent(request, id):
    st = Student.objects.get(id=id)
    st.delete()
    return HttpResponseRedirect("/opensource/students")



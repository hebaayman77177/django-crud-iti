from django import forms
from .models import Student, Track


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "age", "student_track")
        # fields = "__all__"


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ("name",)
        # fields = "__all__"

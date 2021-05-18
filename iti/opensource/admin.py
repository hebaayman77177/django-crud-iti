from django.contrib import admin
from .models import Track, Student


class CustomizedStudent(admin.ModelAdmin):
    fieldsets = (
        ["Students Information", {"fields": ["name", "age", "is_graduated"]}],
        ["scholarship Information", {"fields": ["student_track"]}],
    )
    list_display = ("name", "age", "student_track", "is_graduated")
    list_filter = ["name", "student_track__name"]
    search_fields = ["name", "student_track__name"]


class InlineStudent(admin.StackedInline):
    model = Student
    extra = 5


class CustomizedTrack(admin.ModelAdmin):
    inlines = [InlineStudent]
    list_display = ["name"]


# Register your models here.
admin.site.register(Track, CustomizedTrack)
admin.site.register(Student, CustomizedStudent)

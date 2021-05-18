from django.db import models

# Create your models here.
class Track(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=50)


class Student(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    student_track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        verbose_name="the enroled track",
    )

    def is_graduated(self):
        if self.age > 20:
            return True
        return False

    is_graduated.short_description = "graduated or not"
    is_graduated.boolean = True

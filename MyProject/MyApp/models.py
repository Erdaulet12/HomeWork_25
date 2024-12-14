from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя студента")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса")
    students = models.ManyToManyField(Student, related_name="courses", verbose_name="Студенты")

    def __str__(self):
        return self.title

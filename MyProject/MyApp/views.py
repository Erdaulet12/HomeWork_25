from django.http import HttpResponse
from django.http import JsonResponse
from .models import Student, Course
# Create your views here.


def add_sample_data(request):
    student1 = Student.objects.create(name="Иван Иванов", email="ivan@example.com")
    student2 = Student.objects.create(name="Анна Смирнова", email="anna@example.com")

    course1 = Course.objects.create(title="Python для начинающих", description="Изучение основ Python.")
    course2 = Course.objects.create(title="Веб-разработка на Django", description="Создание веб-приложений с Django.")

    course1.students.add(student1, student2)
    course2.students.add(student2)

    return HttpResponse("Данные успешно добавлены!")


def get_students_and_courses(request):
    students = Student.objects.only("name", "email").prefetch_related("courses")
    data = []

    for student in students:
        courses = student.courses.only("title")
        data.append({
            "student_name": student.name,
            "student_email": student.email,
            "courses": [course.title for course in courses],
        })

    return JsonResponse(data, safe=False)

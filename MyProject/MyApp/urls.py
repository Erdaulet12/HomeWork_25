from django.urls import path
from .views import add_sample_data, get_students_and_courses

urlpatterns = [
    path('add-data/', add_sample_data, name='add_sample_data'),
    path('get-students-and-courses/', get_students_and_courses, name='get_students_and_courses'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('grades/', views.GradeListView.as_view(), name='grade_list'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('<int:id>', views.Student_View, name="student_details"),
    path('delete/<int:id>/', views.Delete_Student, name="delete_student"),
    path('add/', views.add, name='add_student'),
    path('edit/<int:id>/',views.Edit_details, name='edit_student'),
]

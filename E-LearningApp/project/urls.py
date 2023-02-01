"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginPage, name = 'login'),
    path('home/', views.home, name='home'),
    path('view_subjects/', views.view_subjects),
    path('view_subjects/add/<int:id_sub>', views.add_subject),
    path('logout/', views.logoutUser, name='logout'),
    path('subjects/', views.subjects),
    path('subjects/<int:id>', views.get_all_prof_subjects),
    path('subjects/add_new_subject/', views.add_new_subject),
    path('subjects/edit/<int:id>', views.edit_subject),
    path('subjects/delete/<int:id>', views.delete_subject, name='delete_subject'),
    path('subjects/confirm_delete/<int:id>', views.confirm_delete_subject),
    path('subjects/students_enrolled/<int:id>', views.students_enrolled),
    path('subjects/student_list/<int:id_sub>', views.prof_student_list),
    path('subjects/student_list/toggle_status/passed/sub<int:id_sub>/stu<int:id_stu>', views.toggle_to_passed),
    path('subjects/student_list/toggle_status/failed/sub<int:id_sub>/stu<int:id_stu>', views.toggle_to_failed),
    path('students/', views.students),
    path('students/add_new_student/', views.add_new_student),
    path('students/edit/<int:id>', views.edit_student),
    path('students/subjects_enroll/<int:id_stu>', views.subjects_enroll),
    path('students/subjects_enroll/add/sub<int:id_sub>/stu<int:id_stu>', views.add_subjects_enroll),
    path('students/enrollment_form/<int:id_stu>', views.enrollment_form),
    path('students/enrollment_form/confirm_delete/sub<int:id_sub>/stu<int:id_stu>', views.confirm_delete_subject_enrollment_form),
    path('students/enrollment_form/delete/sub<int:id_sub>/stu<int:id_stu>', views.delete_subject_enrollment_form, name="delete_subject_enrollment_form"),
    path('professors/', views.professors),
    path('professors/add_new_professor/', views.add_new_professor),
    path('professors/edit/<int:id>', views.edit_professor),
    path('professors/view_subject_professor/<int:id_prof>', views.view_subject_professor),
    path('professors/view_subject_professor/add/sub<int:id_sub>/prof<int:id_prof>', views.add_subject_professor),
]

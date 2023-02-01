from django.forms import ModelForm
from .models import Korisnik, Predmeti

class AddNewSubjectForm(ModelForm):
    class Meta:
        model = Predmeti
        fields = ['name', 'kod', 'program', 'ects', 'sem_red', 'sem_izv', 'izborni']

class AddNewStudentForm(ModelForm):
    class Meta:
        model = Korisnik
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'role', 'status']

class AddNewProfessorForm(ModelForm):
    class Meta:
        model = Korisnik
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'role', 'status']

class EditNewStudentForm(ModelForm):
    class Meta:
        model = Korisnik
        fields = ['first_name', 'last_name', 'username', 'email', 'role', 'status']

class EditNewProfessorForm(ModelForm):
    class Meta:
        model = Korisnik
        fields = ['first_name', 'last_name', 'username', 'email', 'role', 'status']

class NewUserForm(ModelForm):
    class Meta:
        model = Korisnik
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'role', 'status']
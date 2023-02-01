from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from app.forms import AddNewSubjectForm, AddNewStudentForm, AddNewProfessorForm, EditNewStudentForm, EditNewProfessorForm, NewUserForm
from .models import Korisnik, Upis
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from app.models import Predmeti

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, 'Wrong username or password!')
            
    return render(request, 'login.html')

@login_required
def home(request):
    if request.user.role == "stu":
        subjects = Upis.objects.filter(student_id = request.user.id)
        print(subjects)
        return render(request, 'home.html', {'subjects':subjects})
    return render(request, 'home.html')

@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, 'You have been logout!')
    return redirect("/login")

@login_required
@role_required(allowed_roles=[''])
def subjects(request):
    subjects = Predmeti.objects.all()
    return render(request, 'subjects.html', {'subjects':subjects})
    
@login_required
@role_required(allowed_roles=[''])
def add_new_subject(request):
    form = AddNewSubjectForm()
    if request.method == "POST":
        form = AddNewSubjectForm(request.POST)
        form.save()
        messages.success(request, 'New subject added!')
        return redirect('/subjects/')
    return render(request, 'add_new_subject.html', {'form':form})

@login_required
@role_required(allowed_roles=[''])
def edit_subject(request, id):
    subject = Predmeti.objects.get(id=id)
    if request.method == "POST":
        form = AddNewSubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject successfully edited!')
            return redirect('/subjects/')
    form = AddNewSubjectForm(instance=subject)
    return render(request, 'edit_subject.html', {'form':form})

@login_required
@role_required(allowed_roles=[''])
def confirm_delete_subject(request, id):
    subject = Predmeti.objects.get(id=id)
    return render(request, 'confirm_delete.html', {'subject':subject, 'id':id})

@login_required
@role_required(allowed_roles=[''])
def delete_subject(request, id):
    subject = Predmeti.objects.get(id=id)
    if 'yes' in request.POST:
        subject.delete()
        messages.success(request, 'Subject successfully deleted!')
    return redirect('/subjects/')
    
@login_required
@role_required(allowed_roles=[''])
def students(request):
    students = Korisnik.objects.filter(role="stu")
    return render(request, 'students.html', {'students':students})

@login_required
@role_required(allowed_roles=[''])
def add_new_student(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'New student added!')
            return redirect('/students/')
    return render(request, 'add_new_student.html', {'form':form})

@login_required
@role_required(allowed_roles=[''])
def edit_student(request, id):
    student = Korisnik.objects.get(id=id)
    if request.method == "POST":
        form = NewUserForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student successfully edited!')
            return redirect('/students/')
    form = NewUserForm(instance=student)
    return render(request, 'edit_student.html', {'form':form})

@login_required
@role_required(allowed_roles=[''])
def professors(request):
    professors = Korisnik.objects.filter(role="prof")
    return render(request, 'professors.html', {'professors':professors})

@login_required
@role_required(allowed_roles=[''])
def add_new_professor(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        form.save()
        messages.success(request, 'New professor added!')
        return redirect('/professors/')
    return render(request, 'add_new_professor.html', {'form':form})

@login_required
@role_required(allowed_roles=[''])
def edit_professor(request, id):
    professor = Korisnik.objects.get(id=id)
    if request.method == "POST":
        form = NewUserForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Professor successfully edited!')
            return redirect('/professors/')
    form = NewUserForm(instance=professor)
    return render(request, 'edit_professor.html', {'form':form})

@login_required
@role_required(allowed_roles=[''])
def view_subject_professor(request, id_prof):
    subjects = Predmeti.objects.all()
    return render(request, 'view_subject_professor.html', {'subjects':subjects, 'prof_id':id_prof})

@login_required
@role_required(allowed_roles=[''])
def add_subject_professor(request, id_sub, id_prof):
    subject = Predmeti.objects.get(id=id_sub)
    professor = Korisnik.objects.get(id=id_prof)
    subject.nositelj_predmeta = professor
    subject.save()
    messages.success(request, 'New subject added to professor!')
    return redirect('/professors/')

@login_required
@role_required(allowed_roles=[''])
def subjects_enroll(request, id_stu):
    subjects = Predmeti.objects.all()
    return render(request, 'subjects_enroll.html', {'subjects':subjects, 'id_stu':id_stu})

@login_required
@role_required(allowed_roles=[''])
def add_subjects_enroll(request, id_stu, id_sub):
    student = Korisnik.objects.get(id = id_stu)
    subject = Predmeti.objects.get(id = id_sub)
    upis1 = Upis.objects.filter(predmet_id = id_sub)
    if id_stu in upis1.values_list('student_id', flat=True):
        messages.warning(request, 'Subject already in enrollment form!')
        return redirect('/students/subjects_enroll/' + str(id_stu))
    enroll = Upis(student = student, predmet = subject)
    enroll.save()
    messages.success(request, 'Subject successfully added!')
    return redirect('/students/subjects_enroll/' + str(id_stu))

@login_required
@role_required(allowed_roles=[''])
def enrollment_form(request, id_stu):
    subjects = Upis.objects.filter(student=id_stu)
    return render(request, 'enrollment_form.html', {'subjects':subjects, 'id_stu':id_stu})

@login_required
@role_required(allowed_roles=[''])
def confirm_delete_subject_enrollment_form(request, id_stu, id_sub):
    subject = Upis.objects.get(predmet_id=id_sub)
    return render(request, 'confirm_delete_subject_enrollment_form.html', {'subject':subject, 'id_stu':id_stu, 'id_sub':id_sub})

@login_required
@role_required(allowed_roles=[''])
def delete_subject_enrollment_form(request, id_stu, id_sub):
    subject = Upis.objects.get(predmet_id=id_sub)
    if 'yes' in request.POST:
        subject.delete()
        messages.success(request, 'Subject successfully removed from enrollment form!')
    return redirect('/students/enrollment_form/' + str(id_stu))

@login_required
@role_required(allowed_roles=[''])
def students_enrolled(request, id):
    students = Upis.objects.filter(predmet_id = id)
    return render(request, 'students_enrolled.html', {'students':students})

@login_required
@role_required(allowed_roles=['prof'])
def get_all_prof_subjects(request, id):
    subjects = Predmeti.objects.filter(nositelj_predmeta = id)
    return render(request, 'all_professor_subjects.html', {'subjects':subjects})

@login_required
@role_required(allowed_roles=['prof'])
def prof_student_list(request, id_sub):
    students = Upis.objects.filter(predmet_id = id_sub)
    if request.GET:
        students = students.filter(status = request.GET.get("student"))
    print(students)
    return render(request, 'professor_students_list.html', {'students':students, 'id_sub':id_sub})

@login_required
@role_required(allowed_roles=['prof'])
def toggle_to_passed(request, id_sub, id_stu):
    data = Upis.objects.get(predmet_id = id_sub, student_id = id_stu)
    data.status = "polozen"
    data.save()
    return redirect('/subjects/student_list/' + str(id_sub))

@login_required
@role_required(allowed_roles=['prof'])
def toggle_to_failed(request, id_sub, id_stu):
    data = Upis.objects.get(predmet_id = id_sub, student_id = id_stu)
    data.status = "izgubio potpis"
    data.save() 
    return redirect('/subjects/student_list/' + str(id_sub))

@login_required
@role_required(allowed_roles=['stu'])
def view_subjects(request):
    subjects = Predmeti.objects.all()
    return render(request, 'view_subjects.html', {'subjects':subjects})

@login_required
@role_required(allowed_roles=['stu'])
def add_subject(request, id_sub):
    student = Korisnik.objects.get(id = request.user.id)
    subject = Predmeti.objects.get(id = id_sub)
    upis1 = Upis.objects.filter(predmet_id = id_sub)
    if request.user.id in upis1.values_list('student_id', flat=True):
        messages.warning(request, 'Subject already in enrollment form!')
        return redirect('/view_subjects/')
    enroll = Upis(student = student, predmet = subject)
    enroll.save()
    messages.success(request, 'Subject successfully added!')
    return redirect('/view_subjects/')
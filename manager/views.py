from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Students
from .forms import StudentsForm
# Create your views here.

def main(request):
    return render(request, 'students/index.html',{
        'students': Students.objects.all()
    })

def Student_View(request, id):
    student = Students.objects.get(pk = id)
    return HttpResponseRedirect(reverse('index'))


def Delete_Student(request, id):
    if request.method == 'POST':
        student = Students.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
    

def add(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_cgpa = form.cleaned_data['cgpa']

        new_student = Students(
           student_number = new_student_number,
           first_name = new_first_name ,
           last_name = new_last_name,
           email = new_email,
           field_of_study = new_field_of_study,
           cgpa = new_cgpa
        )   
        new_student.save()

        return render(request, 'students/add.html',{
            'form': StudentsForm(),
            'success': True,
        })
    else:
        form = StudentsForm()
    return render(request, 'students/add.html',{
        'form': StudentsForm(),
    }) 

def Edit_details(request, id):
    if request.method == 'POST':
        student = Students.objects.get(pk = id)
        form = StudentsForm(request.POST, instance=student)   
        if form.is_valid():
            form.save()
            return render(request, "students/Edit.html",{
                'form': form,
                'success': True
            })
    else:
        student = Students.objects.get(pk = id)
        form = StudentsForm(instance=student)
    return render(request, 'students/Edit.html',{
        'form':form
    })    
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from tryHello.models import Student


# Create your views here.
def hello_world(request, name):
    # s1 = Student(name=name, age=10, dob=datetime.date.today())
    # s1.save()
    student = Student.objects.get(name=name)
    student.age = 34
    student.save()
    return HttpResponse("Hello " + student.name + " your age is " + str(student.age))

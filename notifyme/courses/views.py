from django.shortcuts import render,redirect
from .models import *

def add_course(request):
    if request.method=='POST':
        instructor = request.POST['ins']
        course_name = request.POST['cou']
        course_id = request.POST['cid']
        secret_key = request.POST['sk']
        course = Course(instructor=instructor, course_name=course_name, course_id=course_id, secret_key=secret_key)
        course.save()
    else:
        return render(request, 'courses.html')
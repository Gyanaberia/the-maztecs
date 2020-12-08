from django.shortcuts import render
from .models import *

def register(request):
    if request.method=='POST':
        data=request.POST
        print(data)
        username=data[0]
        email=data[1]
        password=data[2]
        stu=Student(username=username, email=email, password=password, course_id=None)
        stu.save()

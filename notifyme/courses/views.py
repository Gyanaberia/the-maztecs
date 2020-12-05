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
        return redirect('/courses/list')
        print("vikas*******************")
    else:
        print("m*******************")
        return render(request, 'courses.html')

def list_courses(request):
    courses=Course.objects.filter(instructor=request.user.username)
    #print(request.user.username)
    # unseen = []
    # for message in messages:
    #     if message.user not in message.seen.all():
    #         message.seen.add(message.user)
    #     if request.user not in message.seen.all():
    #         unseen.append(message)

    return render (request,'list_courses.html',{"obj_list": courses})
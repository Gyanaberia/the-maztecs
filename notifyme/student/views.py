from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import StreamingHttpResponse
from django.http import HttpResponse

@csrf_exempt

def register(request):
    if request.method=='POST':
        received_json_data=json.loads(request.body)
        students=Student.objects.all()
        if(True):
            username=received_json_data['userName']
            email=received_json_data['email']
            password=received_json_data['password']
            stu=Student(username=username, email=email, password=password, course_id=None)
            stu.save()
            return HttpResponse(
            json.dumps({"validStudent": True}),
            content_type="application/json"
            )

        else:
            return HttpResponse(
            json.dumps({"validStudent": True}),
            content_type="application/json"
            )

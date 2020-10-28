from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse
from django.utils import timezone
import json

def notify_create(request):
    if request.method=='POST':
        instructor = request.POST['ins']
        course = request.POST['cou']
        post = Notification.objects.create(instructor = instructor,course = course)
        push_notify(post)
        post.save()
        return redirect('/notify/')
    else:
        return render(request, 'notify.html')

def push_notify(post):
    from pusher_push_notifications import PushNotifications

    beams_client = PushNotifications(
        instance_id='12b1d692-e909-4c13-ab01-9aa733055d56',
        secret_key='01108A9DEA0687F40809FEA53B2667FF8C9EDB40F6EF79118946BDE5816FC899',
    )

    response = beams_client.publish_to_interests(
        interests=['hello'],
        publish_body={
            'apns': {
                'aps': {
                    'alert': 'Message from '+ str(post.instructor)
                }
            },
            'fcm': {
                'notification': {
                    'title': str(post.course),
                    'body': 'You were added to a new course'
                }
            }
        }
    )

    print(response['publishId'])

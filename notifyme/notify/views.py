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
        instance_id='e5e2e6cd-9f3b-449e-a850-3931a46fedc0',
        secret_key='6F61EE51B348051B01FF3C05DB4ED0009322EFBC70A0592CE89E422F21750255',
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

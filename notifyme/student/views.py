from django.shortcuts import render

def register(request):
    data=request.POST
    print(data)

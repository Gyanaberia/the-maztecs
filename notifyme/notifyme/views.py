from django.shortcuts import render,redirect

def student(request):

    print(request.method)
    bulk_data = request.POST
    print(bulk_data)
    Bulk =  request.GET
    print(Bulk)
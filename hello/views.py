from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myview(request):
    oldval = request.COOKIES.get('visit_counter', 1)
    resp = HttpResponse('view count='+ str(oldval))
    print(type(oldval))
    if oldval:
        resp.set_cookie('visit_counter', int(oldval)+1)

    resp.set_cookie('dj4e_cookie', '19696929', max_age=1000)
    return resp
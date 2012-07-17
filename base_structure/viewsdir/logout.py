#coding: utf8
from django.contrib import auth
from django.http    import HttpResponse

def logout(request):
    auth.logout(request)
    return HttpResponse('<h1>Logout Done</h1>')

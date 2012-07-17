#coding: utf8
from django.http      import HttpResponseRedirect
from django.shortcuts import render_to_response

def main(request):
    if request.user.is_authenticated():
        return render_to_response('main.html')
    else:
        return HttpResponseRedirect('/login/')

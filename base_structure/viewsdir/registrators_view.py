#coding: utf8

from django.http      import HttpResponseRedirect
from django.shortcuts import render_to_response

from base_structure.models.registrators       import Registrators
from base_structure.models.registrator_models import Registrator_models


def registrators_view(request):
    if request.user.is_authenticated():
        return render_to_response('registrators.html')
    else:
        return HttpResponseRedirect('/login/')


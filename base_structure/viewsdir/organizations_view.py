#coding: utf8

from django.http           import HttpResponseRedirect
from django.shortcuts      import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from base_structure.models.registrators       import Registrators
from base_structure.models.registrator_models import Registrator_models
from base_structure.models.organizations      import Organizations

from django.views.generic import ListView

def organizations_view(request):
    if request.user.is_authenticated():
        return render_to_response('organizations.html')

    else:
        return HttpResponseRedirect('/login/')

#        organizations_list = Organizations.objects.all()
#
#        paginator = Paginator(organizations_list, 10)
#        try:
#            page = int(request.GET.get('page', '1'))
#        except ValueError:
#            page = 1
#        try:
#            organizations = paginator.page(page)
#        except (EmptyPage, InvalidPage):
#            organizations = paginator.page(paginator.num_pages)
#        return render_to_response('organizations.html', {"organizations": organizations})

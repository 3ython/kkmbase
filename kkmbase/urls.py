from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from base_structure import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kkmbase.views.home', name='home'),
    # url(r'^kkmbase/', include('kkmbase.foo.urls')),
    # url(r'^$', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

     url(r'^$', views.main),

     url(r'^login/$', 'django.contrib.auth.views.login'),

         (r'^logout/$', views.logout),

      url(r'^main.html/$', views.main),
         (r'^organizations.html/$',views.organizations_view),
         (r'^registrators.html/$', views.registrators_view),
         (r'^stampseals.html/$',   views.stampseals_view),
         (r'^workers.html/$',      views.workers_view),
)

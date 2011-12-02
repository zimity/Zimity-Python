from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('zimity.views',
                       
    url(r'^$', 'home'),
   
    url(r'^u/$', 'user_index', name="user_index"),
    url(r'^u/view/(?P<id>\d+)/?$', 'user_view'),
    url(r'^u/add/$', 'user_add'),
    url(r'^u/edit/(?P<id>\d+)/?$', 'user_edit'),
    
    url(r'^i/$', 'imprint_index'),
    url(r'^i/view/(?P<slug>[\w\-]+)/?$', 'imprint_view'),
    url(r'^i/add/$', 'imprint_add'),
    url(r'^i/edit/(?P<id>\d+)/?$', 'imprint_edit'),
    
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    url(r'^about/$', 'about'),
    url(r'^contact/$', 'contact'),
    url(r'^dev/$', 'dev'),
    url(r'^jobs/$', 'jobs'),
    url(r'^privacy/$', 'privacy'),
    url(r'^terms/$', 'terms'),
)
from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('zimity.views',
                       
    url(r'^$', 'home'),
   
    url(r'^users/$', 'user_index', name="user_index"),
    url(r'^users/view/(?P<id>\d+)/?$', 'user_view'),
    url(r'^users/add/$', 'user_add'),
    url(r'^users/edit/(?P<id>\d+)/?$', 'user_edit'),
    
    url(r'^imprint/$', 'imprint_index'),
    url(r'^imprint/view/(?P<slug>[\w\-]+)/?$', 'imprint_view'),
    url(r'^imprint/add/$', 'imprint_add'),
    url(r'^imprint/edit/(?P<id>\d+)/?$', 'imprint_edit'),
    
    url(r'^about/$', 'about'),
    url(r'^contact/$', 'contact'),
    url(r'^dev/$', 'dev'),
    url(r'^jobs/$', 'jobs'),
    url(r'^privacy/$', 'privacy'),
    url(r'^terms/$', 'terms'),
)
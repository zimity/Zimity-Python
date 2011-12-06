from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('zimity.views',
                       
    url(r'^$', 'home', name="home"),
    
    url(r'logout/?$', 'user_logout'),
    
    url('profile/?$', 'user_profile'),
   
    url(r'^u/$', 'user_index', name="user_index"),
    url(r'^u/(?P<username>[\w\-]+)/?$', 'user_view', name="user_view"),
    url(r'^u/add/$', 'user_add'),
    url(r'^u/edit/(?P<id>\d+)/?$', 'user_edit'),
    
    url(r'^i/$', 'imprint_index', name="imprint_index"),

    url(r'^i/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/?$', 'imprint_view', name="imprint_view"),
    url(r'^i/add/$', 'imprint_add'),
    url(r'^i/edit/(?P<id>\d+)/?$', 'imprint_edit'),
    
    url(r'^comments/', include('django.contrib.comments.urls')),
    
)

urlpatterns += patterns('', url(r'login/?$', 'django.contrib.auth.views.login'))
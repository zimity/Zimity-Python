from django.conf.urls.defaults import patterns, include, url

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('zimity.views',
                       
    url(r'^$', 'home'),
   
    url(r'^users/$', 'user_index'),
    url(r'^users/view/(?P<id>\d+)/$', 'user_view'),
    url(r'^users/add/$', 'user_add'),
    url(r'^users/edit/(?P<id>\d+)/$', 'user_edit'),
    
    url(r'^imprint/$', 'imprint_index'),
    url(r'^imprint/view/(?P<id>\d+)/$', 'imprint_view'),
    url(r'^imprint/add/$', 'imprint_add'),
    url(r'^imprint/edit/(?P<id>\d+)/$', 'imprint_edit'),
    
    url(r'^about/$', 'about'),
    url(r'^contact/$', 'contact'),
    url(r'^dev/$', 'dev'),
    url(r'^jobs/$', 'jobs'),
    url(r'^privacy/$', 'privacy'),
    url(r'^terms/$', 'terms'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve',  {'document_root': settings.MEDIA_ROOT}))
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^Spork/', include('Spork.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sporkapp.views.subscribe'),
    url(r'^home/$', 'sporkapp.views.home'),
    url(r'^subscribe/$', 'sporkapp.views.subscribe'),
    url(r'^donations/$', 'sporkapp.views.donations'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : '/home/manvsmachine/Spork/Spork/sporkapp/media/'}),
    url(r'^admin/$', include(admin.site.urls))
)

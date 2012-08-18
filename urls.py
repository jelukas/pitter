from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/', include('pitter.registration.backends.default.urls')),
    # Examples:
    # url(r'^$', 'usuarios.views.home', name='home'),
    # url(r'^usuarios/', include('usuarios.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^pitter/', include('pitapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

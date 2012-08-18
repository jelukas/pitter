from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^test/', 'pitapp.views.profile_test'),
)

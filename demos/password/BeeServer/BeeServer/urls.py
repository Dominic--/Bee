from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BeeServer.views.home', name='home'),
    # url(r'^BeeServer/', include('BeeServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'service.views.list', name='list'),
    url(r'^set/', 'service.views.set', name='set'),
    url(r'^get/', 'service.views.get', name='get'),
)

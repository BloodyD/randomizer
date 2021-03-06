from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', 'randomizer.views.index', name='index'),
    url(r'^$', 'randomizer.views.update', name='index'),

    url(r'^login/$', 'randomizer.views.login'),
    url(r'^logout/$', 'randomizer.views.logout'),

    url(r'^ajax/submit/$', 'randomizer.views.submit'),
    url(r'^ajax/update/$', 'randomizer.views.get_update'),
    # url(r'^randomizer/', include('randomizer.foo.urls')),

    (r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),
    (r'^media/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

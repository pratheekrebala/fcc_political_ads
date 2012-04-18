from django.conf.urls import patterns, include, url


urlpatterns = patterns('broadcasters',
    url(r'^state/(?P<state_id>\w{2})/$', 'views.state_broadcaster_list', name='broadcaster_state_list'),
    # url(r'^state/$', 'views.state_broadcaster_list', name='broadcaster_state_list'),
    url(r'^nearby.json$', 'views.nearest_broadcasters_list', name='nearest_broadcasters_list'),
    url(r'^station/(?P<callsign>[\w-]+)/$', 'views.broadcaster_detail', name='broadcaster_detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import polls.views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurants.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', polls.views.main_site),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),


    #url(r'^main_site/$', polls.views.main_site),


    # url(r'^votes/$', polls.views.votes),
    # url(r'^stadistics/$', polls.views.stadistics),

)

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pangea_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'user_app.views.landing', name='landing'),
    url(r'^giver/$', 'giver_app.views.giver_home', name='giver_home'),
    url(r'^charity/$', 'charity_app.views.charity_home', name='charity_home'),
)

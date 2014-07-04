from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()
from tastypie.api import Api



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pangea_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^login/$', 'user_app.views.login1', name='login1'),
    # url(r'^register/$', 'user_app.views.signup', name='signup'),


    url('', include('social.apps.django_app.urls', namespace='social')),


    url(r'^giver/create/$', 'giver_app.views.giver_create', name='giver_create'),
    url(r'^giver/$', 'giver_app.views.giver_landing', name='giver_landing'),

    url(r'^charity/dashboard/$', 'charity_app.views.charity_dashboard', name='charity_dashboard'),
    url(r'^charity/create/$', 'charity_app.views.charity_create', name='charity_create'),
    url(r'^charity/$', 'charity_app.views.charity_landing', name='charity_landing'),

    url(r'^$', 'user_app.views.home_page', name='home_page'),

    url(r'^secret/$', 'user_app.views.special_page', name='secret'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^accounts/password/change/$',
        auth_views.password_change,
        name='password_change'),
    url(r'^accounts/password/change/done/$',
        auth_views.password_change_done,
        name='password_change_done'),
    url(r'^accounts/password/reset/$',
        auth_views.password_reset,
        name='password_reset'),
    url(r'^accounts/password/reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^accounts/password/reset/complete/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'', include('registration.backends.default.urls')),

    url(r'^s3direct/', include('s3direct.urls'))
)

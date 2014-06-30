from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pangea_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'user_app.views.index', name='index'),
    # url(r'^login/$', 'user_app.views.login1', name='login1'),
    # url(r'^register/$', 'user_app.views.signup', name='signup'),
    url(r'^giver/$', 'giver_app.views.giver_home', name='giver_home'),
    url(r'^charity/$', 'charity_app.views.charity_home', name='charity_home'),
    url(r'^secret/$', 'user_app.views.special_page', name='secret'),
    # url(r'^accounts/login$', 'auth_app.views.login1', name='login'),
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
      #url(r'', include('registration.backends.default.urls')),

    url(r'^s3direct/', include('s3direct.urls'))
)
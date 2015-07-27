from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'workout.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'workout.views.bloglist', name='bloglist'),
	url(r'^(?P<list_id>\d+)/$', 'workout.views.blogdetail', name='blogdetail'),
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'mysite.views.error404'

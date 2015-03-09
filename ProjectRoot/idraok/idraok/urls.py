from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'idraok.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$','article.views.hello'),		#1st arguement is the def function name, 2nd roots to article.views.hello
	url(r'^hello_template/$','article.views.hello_template'),
)

from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^ulog/', include('ulog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^detail/$','Software.views.login'),
    url(r'^perform/$','Software.views.try_to_login'),
    url(r'^edit/$','Article.views.edit_profile'),
    url(r'^login/$','Article.views.login'),
    url(r'^logout/$','Article.views.logout'),    
    url(r'^articles/$','Article.views.create'),
    url(r'^articles/all/$','Article.views.main'),
    url(r'^page=(\d{1,2})/pages/$','Article.views.main_offset'),
    url(r'^load/(\d{1,2})/$','Article.views.load_article'),
    url(r'^search/$', 'Article.views.search_titles'),
    url(r'^chg_passwd/$', 'Article.views.change_password'),
    url(r'^passwd/$', 'Article.views.passwd'),
    url(r'^forgot_passwd/$', 'Article.views.forgot_password'),
    url(r'^forgot_chg_passwd/$', 'Article.views.forgot_change_password'),
    url(r'^add_user/$', 'Article.views.add_user'),
    url(r'^front/$', 'Article.views.front'),
    url(r'^guest/$','Article.views.guest'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

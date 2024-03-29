from django.conf.urls import include, url
from django.contrib import admin

import pgcommitfest.commitfest.views as views
import pgcommitfest.commitfest.reports as reports
import pgcommitfest.commitfest.ajax as ajax
import pgcommitfest.commitfest.lookups as lookups
import pgcommitfest.auth
import pgcommitfest.userprofile.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', views.home),
    url(r'^activity(?P<rss>\.rss)?/', views.activity),
    url(r'^(\d+)/$', views.commitfest),
    url(r'^(open|inprogress)/$', views.redir),
    url(r'^(?P<cfid>\d+)/activity(?P<rss>\.rss)?/$', views.activity),
    url(r'^(\d+)/(\d+)/$', views.patch),
    url(r'^(\d+)/(\d+)/edit/$', views.patchform),
    url(r'^(\d+)/new/$', views.newpatch),
    url(r'^(\d+)/(\d+)/status/(review|author|committer)/$', views.status),
    url(r'^(\d+)/(\d+)/close/(reject|withdrawn|feedback|committed|next)/$', views.close),
    url(r'^(\d+)/(\d+)/reviewer/(become|remove)/$', views.reviewer),
    url(r'^(\d+)/(\d+)/committer/(become|remove)/$', views.committer),
    url(r'^(\d+)/(\d+)/(un)?subscribe/$', views.subscribe),
    url(r'^(\d+)/(\d+)/(comment|review)/', views.comment),
    url(r'^(\d+)/send_email/$', views.send_email),
    url(r'^(\d+)/\d+/send_email/$', views.send_email),
    url(r'^(\d+)/reports/authorstats/$', reports.authorstats),
    url(r'^search/$', views.global_search),
    url(r'^ajax/(\w+)/$', ajax.main),
    url(r'^lookups/user/$', lookups.userlookup),
    url(r'^thread_notify/$', views.thread_notify),

    # Auth system integration
    url(r'^(?:account/)?login/?$', pgcommitfest.auth.login),
    url(r'^(?:account/)?logout/?$', pgcommitfest.auth.logout),
    url(r'^auth_receive/$', pgcommitfest.auth.auth_receive),
    url(r'^auth_api/$', pgcommitfest.auth.auth_api),

    # Account management
    url(r'^account/profile/$', pgcommitfest.userprofile.views.userprofile),

    # Examples:
    # url(r'^$', 'pgpgcommitfest.commitfest.views.home', name='home),
    # url(r'^pgcommitfest/', include('pgcommitfest.foo.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]

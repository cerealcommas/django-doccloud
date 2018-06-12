# from django.conf.urls import url, patterns
# from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import include, re_path
# from django.conf.urls.defaults import url

urlpatterns = patterns('',
    re_path(r'^$', 'doccloud.views.list', name='docs_list'),
    re_path(r'^list/$', 'doccloud.views.list', name='docs_list'),
    re_path(r'^detail/(?P<slug>[\w-]+)/$', 'doccloud.views.detail',
        name='docs_detail'),
    re_path(r'^create/$', 'doccloud.views.create', name='docs_create'),
    re_path(r'^upload/$', 'doccloud.views.upload', name='docs_upload'),
)

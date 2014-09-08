# -*- coding: utf-8 -*-

from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns('',
    url(r'^redir/', include('project.redir.urls')),
    ) + urlpatterns

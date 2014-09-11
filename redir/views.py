# Create your views here.

from django.http import Http404  
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from .models import Redirect


class RedirView(RedirectView):
    permanent = False

    def get_redirect_url(self, **kwargs):
        redirect_website = None
        my_languages = []
        try:
            browser_languages = self.request.META['HTTP_ACCEPT_LANGUAGE'].split(';')[0].split(',')
        except KeyError:
            browser_languages = ['en']
        redir_obj = get_object_or_404(Redirect, slug=self.kwargs['slug'])
        accepted_languages = redir_obj.language_urls.all().values_list('language', flat=True)
        for lang in browser_languages:
            if lang not in my_languages:
                my_languages.append(lang)
            if lang.split('-')[0] not in my_languages:
                my_languages.append(lang.split('-')[0])
        for lang in my_languages:
            if lang in accepted_languages:
                redirect_website = redir_obj.language_urls.get(language=lang)
                break
        if not redirect_website:
            if 'en' in accepted_languages:
                redirect_website = redir_obj.language_urls.get(language="en")
                return redirect_website.url
            elif redir_obj.language_urls.all().exists():
                redirect_website = redir_obj.language_urls.all().order_by('language')[0:1][0]
            else:
                raise Http404
        return redirect_website.url

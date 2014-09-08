from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.


class LanguageURL(models.Model):
    language = models.CharField(_('language'), max_length=20)
    url = models.URLField(_('URL'), max_length=100, null=True)

    def __unicode__(self):
        return '%s - %s' % (self.language, self.url)


class Redirect(models.Model):
    slug = models.SlugField(null=True)
    language_urls = models.ManyToManyField(LanguageURL)

    def __unicode__(self):
        return '%s' % (self.slug)

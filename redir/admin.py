from django.contrib import admin
from django import forms
from django.utils.translation import ugettext as _
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Redirect, LanguageURL


class RedirectAdminForm(forms.ModelForm):
    # language_urls = forms.ModelMultipleChoiceField(
    #                     queryset=LanguageURL.objects.all(),
    #                     widget=FilteredSelectMultiple(_('LanguageURL'), False))
    
    class Meta:
        model = Redirect


class RedirectAdmin(admin.ModelAdmin):
    form = RedirectAdminForm



admin.site.register(Redirect, RedirectAdmin)
admin.site.register(LanguageURL)

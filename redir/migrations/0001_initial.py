# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LanguageURL'
        db.create_table(u'redir_languageurl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'redir', ['LanguageURL'])

        # Adding model 'Redirect'
        db.create_table(u'redir_redirect', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True)),
        ))
        db.send_create_signal(u'redir', ['Redirect'])

        # Adding M2M table for field language_urls on 'Redirect'
        m2m_table_name = db.shorten_name(u'redir_redirect_language_urls')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('redirect', models.ForeignKey(orm[u'redir.redirect'], null=False)),
            ('languageurl', models.ForeignKey(orm[u'redir.languageurl'], null=False))
        ))
        db.create_unique(m2m_table_name, ['redirect_id', 'languageurl_id'])


    def backwards(self, orm):
        # Deleting model 'LanguageURL'
        db.delete_table(u'redir_languageurl')

        # Deleting model 'Redirect'
        db.delete_table(u'redir_redirect')

        # Removing M2M table for field language_urls on 'Redirect'
        db.delete_table(db.shorten_name(u'redir_redirect_language_urls'))


    models = {
        u'redir.languageurl': {
            'Meta': {'object_name': 'LanguageURL'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True'})
        },
        u'redir.redirect': {
            'Meta': {'object_name': 'Redirect'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_urls': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['redir.LanguageURL']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['redir']
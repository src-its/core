# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Issue'
        db.create_table(u'ca_wiki_issue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue_summary', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('issue_elaboration', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('issue_opened', self.gf('django.db.models.fields.DateTimeField')()),
            ('issue_closed', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'ca_wiki', ['Issue'])

        # Adding model 'Instructions'
        db.create_table(u'ca_wiki_instructions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('step', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'ca_wiki', ['Instructions'])


    def backwards(self, orm):
        # Deleting model 'Issue'
        db.delete_table(u'ca_wiki_issue')

        # Deleting model 'Instructions'
        db.delete_table(u'ca_wiki_instructions')


    models = {
        u'ca_wiki.instructions': {
            'Meta': {'object_name': 'Instructions'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'step': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ca_wiki.issue': {
            'Meta': {'object_name': 'Issue'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_closed': ('django.db.models.fields.BooleanField', [], {}),
            'issue_elaboration': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'issue_opened': ('django.db.models.fields.DateTimeField', [], {}),
            'issue_summary': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ca_wiki']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Giver'
        db.create_table(u'giver_app_giver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('business_url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=6000, null=True, blank=True)),
            ('cover_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('background_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('video', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'giver_app', ['Giver'])


    def backwards(self, orm):
        # Deleting model 'Giver'
        db.delete_table(u'giver_app_giver')


    models = {
        u'giver_app.giver': {
            'Meta': {'object_name': 'Giver'},
            'background_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'business_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cover_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '6000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['giver_app']
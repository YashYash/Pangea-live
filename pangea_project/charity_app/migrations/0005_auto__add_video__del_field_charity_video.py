# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table(u'charity_app_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('charity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='charities', to=orm['charity_app.Charity'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('video_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'charity_app', ['Video'])

        # Deleting field 'Charity.video'
        db.delete_column(u'charity_app_charity', 'video')


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'charity_app_video')

        # Adding field 'Charity.video'
        db.add_column(u'charity_app_charity', 'video',
                      self.gf('django.db.models.fields.URLField')(default=datetime.datetime(2014, 6, 30, 0, 0), max_length=200),
                      keep_default=False)


    models = {
        u'charity_app.charity': {
            'Meta': {'object_name': 'Charity'},
            'background_image': ('s3direct.fields.S3DirectField', [], {}),
            'charity_url': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'cover_photo': ('s3direct.fields.S3DirectField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '6000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('s3direct.fields.S3DirectField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'statement': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        u'charity_app.video': {
            'Meta': {'object_name': 'Video'},
            'charity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'charities'", 'to': u"orm['charity_app.Charity']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['charity_app']
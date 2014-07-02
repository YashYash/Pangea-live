# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Charity.background_image'
        db.alter_column(u'charity_app_charity', 'background_image', self.gf('s3direct.fields.S3DirectField')(null=True))

        # Changing field 'Charity.image'
        db.alter_column(u'charity_app_charity', 'image', self.gf('s3direct.fields.S3DirectField')(null=True))

        # Changing field 'Charity.cover_photo'
        db.alter_column(u'charity_app_charity', 'cover_photo', self.gf('s3direct.fields.S3DirectField')(null=True))

    def backwards(self, orm):

        # Changing field 'Charity.background_image'
        db.alter_column(u'charity_app_charity', 'background_image', self.gf('s3direct.fields.S3DirectField')(default=datetime.datetime(2014, 7, 2, 0, 0)))

        # User chose to not deal with backwards NULL issues for 'Charity.image'
        raise RuntimeError("Cannot reverse this migration. 'Charity.image' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Charity.image'
        db.alter_column(u'charity_app_charity', 'image', self.gf('s3direct.fields.S3DirectField')())

        # Changing field 'Charity.cover_photo'
        db.alter_column(u'charity_app_charity', 'cover_photo', self.gf('s3direct.fields.S3DirectField')(default=datetime.datetime(2014, 7, 2, 0, 0)))

    models = {
        u'charity_app.charity': {
            'Meta': {'object_name': 'Charity'},
            'background_image': ('s3direct.fields.S3DirectField', [], {'null': 'True', 'blank': 'True'}),
            'charity_url': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'cover_photo': ('s3direct.fields.S3DirectField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '6000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('s3direct.fields.S3DirectField', [], {'null': 'True', 'blank': 'True'}),
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
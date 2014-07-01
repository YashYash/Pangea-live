# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Charity.background_image'
        db.alter_column(u'charity_app_charity', 'background_image', self.gf('s3direct.fields.S3DirectField')(default=datetime.datetime(2014, 6, 30, 0, 0)))

        # Changing field 'Charity.image'
        db.alter_column(u'charity_app_charity', 'image', self.gf('s3direct.fields.S3DirectField')(default=datetime.datetime(2014, 6, 30, 0, 0)))

        # Changing field 'Charity.cover_photo'
        db.alter_column(u'charity_app_charity', 'cover_photo', self.gf('s3direct.fields.S3DirectField')(default=datetime.datetime(2014, 6, 30, 0, 0)))

    def backwards(self, orm):

        # Changing field 'Charity.background_image'
        db.alter_column(u'charity_app_charity', 'background_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Charity.image'
        db.alter_column(u'charity_app_charity', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Charity.cover_photo'
        db.alter_column(u'charity_app_charity', 'cover_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

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
            'statement': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['charity_app']
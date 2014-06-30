# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Giver.background_image'
        db.alter_column(u'giver_app_giver', 'background_image', self.gf('s3direct.fields.S3DirectField')(default=datetime.datetime(2014, 6, 30, 0, 0)))

        # Changing field 'Giver.image'
        db.alter_column(u'giver_app_giver', 'image', self.gf('s3direct.fields.S3DirectField')(default=datetime.datetime(2014, 6, 30, 0, 0)))

        # Changing field 'Giver.cover_photo'
        db.alter_column(u'giver_app_giver', 'cover_photo', self.gf('s3direct.fields.S3DirectField')(default=datetime.datetime(2014, 6, 30, 0, 0)))

    def backwards(self, orm):

        # Changing field 'Giver.background_image'
        db.alter_column(u'giver_app_giver', 'background_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Giver.image'
        db.alter_column(u'giver_app_giver', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Giver.cover_photo'
        db.alter_column(u'giver_app_giver', 'cover_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    models = {
        u'giver_app.giver': {
            'Meta': {'object_name': 'Giver'},
            'background_image': ('s3direct.fields.S3DirectField', [], {}),
            'business_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cover_photo': ('s3direct.fields.S3DirectField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '6000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('s3direct.fields.S3DirectField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['giver_app']
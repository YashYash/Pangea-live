# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field charities on 'Giver'
        m2m_table_name = db.shorten_name(u'giver_app_giver_charities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('giver', models.ForeignKey(orm[u'giver_app.giver'], null=False)),
            ('charity', models.ForeignKey(orm[u'charity_app.charity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['giver_id', 'charity_id'])


        # Changing field 'Giver.background_image'
        db.alter_column(u'giver_app_giver', 'background_image', self.gf('s3direct.fields.S3DirectField')(null=True))

        # Changing field 'Giver.image'
        db.alter_column(u'giver_app_giver', 'image', self.gf('s3direct.fields.S3DirectField')(null=True))

        # Changing field 'Giver.cover_photo'
        db.alter_column(u'giver_app_giver', 'cover_photo', self.gf('s3direct.fields.S3DirectField')(null=True))

    def backwards(self, orm):
        # Removing M2M table for field charities on 'Giver'
        db.delete_table(db.shorten_name(u'giver_app_giver_charities'))


        # Changing field 'Giver.background_image'
        db.alter_column(u'giver_app_giver', 'background_image', self.gf('s3direct.fields.S3DirectField')(default=datetime.datetime(2014, 6, 30, 0, 0)))

        # Changing field 'Giver.image'
        db.alter_column(u'giver_app_giver', 'image', self.gf('s3direct.fields.S3DirectField')(default=datetime.datetime(2014, 6, 30, 0, 0)))

        # Changing field 'Giver.cover_photo'
        db.alter_column(u'giver_app_giver', 'cover_photo', self.gf('s3direct.fields.S3DirectField')(default=datetime.datetime(2014, 6, 30, 0, 0)))

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
        u'giver_app.giver': {
            'Meta': {'object_name': 'Giver'},
            'background_image': ('s3direct.fields.S3DirectField', [], {'null': 'True', 'blank': 'True'}),
            'business_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'charities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'givers'", 'symmetrical': 'False', 'to': u"orm['charity_app.Charity']"}),
            'cover_photo': ('s3direct.fields.S3DirectField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '6000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('s3direct.fields.S3DirectField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['giver_app']
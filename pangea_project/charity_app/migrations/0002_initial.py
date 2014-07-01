class Migration(SchemaMigration):

    def forwards(self, orm):
        pass
        # Adding model 'Charity'
        db.create_table(u'charity_app_charity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('charity_url', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('statement', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=6000, null=True, blank=True)),
            ('cover_photo', self.gf('s3direct.fields.S3DirectField')()),
            ('background_image', self.gf('s3direct.fields.S3DirectField')()),
            ('image', self.gf('s3direct.fields.S3DirectField')()),
        ))
        db.send_create_signal(u'charity_app', ['Charity'])

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


    def backwards(self, orm):
        pass
        # Deleting model 'Charity'
        db.delete_table(u'charity_app_charity')

        # Deleting model 'Video'
        db.delete_table(u'charity_app_video')


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

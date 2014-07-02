from django.db import models
from embed_video.fields import EmbedVideoField
from s3direct.fields import S3DirectField
from django.contrib.auth.models import User
# Create your models here.

class Charity(models.Model):
    name = models.CharField(max_length=200, null=True)
    posted = models.DateTimeField(auto_now=True)
    charity_url = models.CharField(max_length=1000, null=True, blank=True)
    slogan = models.CharField(max_length=200, null=True, blank=True)
    statement = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=6000, null=True, blank=True)
    cover_photo = S3DirectField(upload_to='s3direct', null=True, blank=True)
    background_image = S3DirectField(upload_to='s3direct', null=True, blank=True)
    image = S3DirectField(upload_to='s3direct', null=True, blank=True)
    user = models.OneToOneField(User, related_name="charity", null=True, blank=True)

    def __unicode__(self):
        return self.name


class Video(models.Model):
    charity = models.ForeignKey(Charity, related_name="charities")
    title = models.CharField(max_length=250)
    posted = models.DateTimeField(auto_now=True)
    video_url = models.URLField()
    description = models.CharField(max_length=200, null=True)
    video_embed = EmbedVideoField()

    def __unicode__(self):
        return self.title
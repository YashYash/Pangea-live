from django.db import models
from s3direct.fields import S3DirectField
from charity_app.models import Charity


class Giver(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    posted = models.DateTimeField(auto_now=True)
    business_url = models.CharField(max_length=200, null=True, blank=True)
    slogan = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=6000, null=True, blank=True)
    cover_photo = S3DirectField(upload_to='s3direct', null=True, blank=True)
    background_image = S3DirectField(upload_to='s3direct', null=True, blank=True)
    image = S3DirectField(upload_to='s3direct', null=True, blank=True)
    video = models.URLField()
    charities = models.ManyToManyField(Charity, related_name="givers")

    def __unicode__(self):
        return self.name


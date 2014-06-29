from django.db import models

# Create your models here.

class Charity(models.Model):
    name = models.CharField(max_length=200, null=True)
    posted = models.DateTimeField(auto_now=True)
    charity_url = models.CharField(max_length=1000, null=True, blank=True)
    slogan = models.CharField(max_length=200, null=True, blank=True)
    statement = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=6000, null=True, blank=True)
    cover_photo = models.ImageField(upload_to="images/charity_coverphoto", null=True, blank=True)
    background_image = models.ImageField(upload_to="images/charity_background", null=True, blank=True)
    image = models.ImageField(upload_to="images/charity_logo", null=True, blank=True)
    video = models.URLField()

    def __unicode__(self):
        return self.name


from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from autoslug.fields import AutoSlugField

User._meta.ordering = ['-last_login']

class UserProfile(models.Model):
    # required field
    user = models.OneToOneField(User)
    
    quote = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=20, blank=True)
    about = models.TextField(blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    google = models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
        return self.user.first_name
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
    
class Imprint(models.Model):
    class Meta:
        ordering = ['-created']
        
    def get_absolute_url(self):
        return "/i/%s/%s" % (self.created.strftime("%Y/%m/%d").lower(), self.slug)

    NOTE = 1
    PHOTO = 2
    AUDIO = 3
    VIDEO = 4
    REMINDER = 5
    EVENT = 6
    DEAL = 7
    BOOKMARK = 8
    
    IMPRINT_TYPE = (
        (NOTE, 'NOTE'),
        (PHOTO, 'PHOTO'),
        (AUDIO, 'AUDIO'),
        (VIDEO, 'VIDEO'),
        (REMINDER, 'REMINDER'),
        (EVENT, 'EVENT'),
        (DEAL, 'DEAL'),
        (BOOKMARK, 'BOOKMARK'),
    )
    
    PRIVATE = 1
    FRIENDS = 2
    GLOBAL = 3
    
    SHARING_SCOPE = (
        (1, 'PRIVATE'),
        (2, 'FRIENDS'),
        (3, 'GLOBAL'),
    )
    
    user = models.ForeignKey(User)
    slug = AutoSlugField(populate_from='title', unique_with='created')
    type = models.IntegerField(choices=IMPRINT_TYPE)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=16,decimal_places=13)
    longitude = models.DecimalField(max_digits=16,decimal_places=13)
    altitude = models.IntegerField()
    bearing = models.IntegerField()
    speed = models.IntegerField()
    sharing = models.IntegerField(choices=SHARING_SCOPE)
    accuracy = models.IntegerField()
    deleted = models.BooleanField()
    created = models.DateTimeField('date created',auto_now_add=True)
    modified = models.DateTimeField('date modified',auto_now=True)

    def __unicode__(self):
        return self.title
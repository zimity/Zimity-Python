from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # required field
    user = models.OneToOneField(User)
    
    quote = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    about = models.TextField()
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    google = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.user.first_name
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
    
class Imprint(models.Model):
    user = models.ForeignKey(User)
    slug = models.SlugField(max_length=6)
    imp_type = models.IntegerField()
    title = models.CharField(max_length=50)
    content = models.TextField()
    latitude = models.DecimalField(max_digits=16,decimal_places=13)
    longitude = models.DecimalField(max_digits=16,decimal_places=13)
    altitude = models.IntegerField()
    bearing = models.IntegerField()
    speed = models.IntegerField()
    sharing = models.IntegerField()
    accuracy = models.IntegerField()
    deleted = models.BooleanField()
    created = models.DateTimeField('date created',auto_now_add=True)
    modified = models.DateTimeField('date modified',auto_now=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    imprint = models.ForeignKey(Imprint)
    user = models.ForeignKey(User, related_name='user_comment')
    content = models.TextField()
    deleted = models.BooleanField()
    created = models.DateTimeField('date created',auto_now_add=True)
    modified = models.DateTimeField('date modified',auto_now=True)

    def __unicode__(self):
        return self.content
    
    
class Message(models.Model):
    user = models.ForeignKey(User)
    recipient = models.ForeignKey(User, related_name='recipient_message')
    content = models.TextField()
    deleted = models.BooleanField()
    created = models.DateTimeField('date created',auto_now_add=True)
    modified = models.DateTimeField('date modified',auto_now=True)
    
    def __unicode__(self):
        return self.content
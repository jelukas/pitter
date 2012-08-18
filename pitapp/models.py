from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,unique=True)
    topic = models.CharField(max_length = 160)
    location = models.CharField(max_length = 50)

    def __unicode__(self):
        return "%s's profile" % self.user

class Follow(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    follower = models.ForeignKey(User, related_name='following')
    followed = models.ForeignKey(User, related_name='followers')

    def __unicode__(self):
        return self.follower.username + " is following " + self.followed.username

class Pit(models.Model):
	content = models.TextField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True, blank=False)
	deleted = models.BooleanField()
	user = models.ForeignKey(User, related_name='pits')

# Signals
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,topic = "Soy un Nuevo usuario")

post_save.connect(create_user_profile, sender=User, dispatch_uid="users-profile-creation-signal")
from django.contrib.auth.models import User
from django.db import models
import requests
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

# Did you want to make a separate model with a one to one relationship instead
# of making Profile and AbstractUser?
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', primary_key=True)
    picture = models.ImageField(null=True, upload_to='profile_pics')
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return 'Profile: {}'.format(self.user.username)


class Telephone(models.Model):
    sound_url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='telephones')
    
    # Glad you made these relationships!
    
    # This is still a bit not DRY from a database standpoint, but may simplify code or speed up performances somewhere.
    # Technically from the original Telephone, you can keep looping through all of the children and don't need the `owner` field.
    original = models.ForeignKey('self', null=True, blank=True, related_name='copies')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child')

    def get_sound_url(self):
        url = 'http://tts-api.com/tts.mp3?q={}&return_url=1'.format(self.text)
        res = requests.get(url)
        # should there be error checking here?
        self.sound_url = res.text

    def pass_it_on(self, changed_text, new_owner):
        copy = Telephone.objects.create(
            text=changed_text,
            owner=new_owner,
            original=self.original if self.original else self,
            parent=self
        )
        # might be better named `set_sound_url` instead of get
        copy.get_sound_url()
        return copy

    def __unicode__(self):
        return '{}: {}'.format(self.owner.username, self.text)

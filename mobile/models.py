from django.contrib.auth.models import User
from django.db import models
import requests


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', primary_key=True)
    picture = models.ImageField(null=True, upload_to='profile_pics')
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '{}: {}'.format(self.user.username, self.description)


class Telephone(models.Model):
    sound_url = models.URLField(null=True)
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='telephones')
    original = models.ForeignKey('self', null=True, related_name='copies')
    parent = models.ForeignKey('self', null=True, related_name='child')

    def get_sound_url(self):
        url = 'http://tts-api.com/tts.mp3?q={}&return_url=1'.format(self.text)
        res = requests.get(url)
        self.sound_url = res.text

    def pass_it_on(self, changed_text, new_owner):
        copy = Telephone.objects.create(
            text=changed_text,
            owner=new_owner,
            original=self.original if self.original else self,
            parent=self
        )
        copy.get_sound_url()
        return copy

    def __unicode__(self):
        return '{}: {}'.format(self.owner.username, self.text)

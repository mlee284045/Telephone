from django.contrib.auth.models import User
from django.db import models
import requests


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    picture = models.ImageField(null=True)
    description = models.TextField(blank=True, null=True)


class Telephone(models.Model):
    sound_url = models.URLField(null=True)
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='telephone')
    original = models.PositiveSmallIntegerField(null=True)
    # Little hacky but will contain pk's of copies by concatenating them to the string
    copies = models.CommaSeparatedIntegerField(max_length=200, null=True)

    def update_copies(self, new_pk):
        print 'UPDATE'
        print '-{}-'.format(self.copies)
        self.copies += ',{}'.format(new_pk)
        self.save(update_fields=['copies'])
        print '--{}--'.format(self.copies)

    def get_sound_url(self):
        url = 'http://tts-api.com/tts.mp3?q={}&return_url=1'.format(self.text)
        res = requests.get(url)
        self.sound_url = res.text

    def pass_it_on(self, changed_text, new_owner):
        copy = Telephone.objects.create(
            text=changed_text,
            owner=new_owner,
            original=self.original if self.original else self.pk
        )
        copy.get_sound_url()
        if self.original:
            orig_telephone = Telephone.objects.get(pk=copy.original)
            orig_telephone.copies += ',{}'.format(copy.pk)
            Telephone.objects.filter(pk=copy.original).update(copies=orig_telephone.copies)
            print 'YOOO=={}==HOOO'.format(Telephone.objects.get(pk=copy.original).copies)
        else:
            self.update_copies(copy.pk)
        return copy

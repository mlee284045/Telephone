from django.contrib.auth.models import User
from django.test import TestCase
from mobile.models import Telephone


class ModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@test.com',
            password='user1'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@test.com',
            password='user2'
        )
        self.user3 = User.objects.create_user(
            username='user3',
            email='user3@test.com',
            password='user3'
        )
        self.user4 = User.objects.create_user(
            username='user4',
            email='user4@test.com',
            password='user4'
        )
        self.orig = Telephone.objects.create(
            owner=self.user1,
            text='She sells seashells',
            copies=''
        )

    def test_get_sound_url(self):
        self.assertIsNone(self.orig.sound_url)
        self.orig.get_sound_url()
        self.assertIsNotNone(self.orig.sound_url)

    def test_pass_it_on(self):
        print self.orig.pk
        self.assertEqual(self.orig.copies, '')
        copy1 = self.orig.pass_it_on(
            changed_text='See shells she sells',
            new_owner=self.user2
        )
        print 'CREATE COPY 1'
        print 'original - |{}|'.format(copy1.original)
        print '---{}---'.format(self.orig.copies)
        self.assertEqual(self.orig.copies, ',{}'.format(copy1.pk))
        self.assertEqual(copy1.original, self.orig.pk)
        self.assertIsNotNone(copy1.sound_url)

        copy2 = copy1.pass_it_on(
            changed_text='See sells see sells',
            new_owner=self.user3
        )
        print 'CREATE COPY 2'
        print 'original - |{}|'.format(copy2.original)
        print '---{}---'.format(self.orig.copies)
        self.assertEqual(self.orig.copies, ',{},{}'.format(copy1.pk, copy2.pk))
        self.assertEqual(copy2.original, self.orig.pk)
        self.assertIsNotNone(copy2.sound_url)

        copy3 = copy2.pass_it_on(
            changed_text='She sells sea smells',
            new_owner=self.user4
        )
        print 'CREATE COPY 3'
        print '---{}---'.format(self.orig.copies)
        self.assertEqual(self.orig.copies, '{},{},{}'.format(copy1.pk, copy2.pk, copy3.pk))
        self.assertEqual(copy3.original, self.orig.pk)
        self.assertIsNotNone(copy3.sound_url)

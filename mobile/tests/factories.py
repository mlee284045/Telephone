import factory


class TelephoneFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'mobile.Telephone'

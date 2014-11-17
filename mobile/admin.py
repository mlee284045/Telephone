from django.contrib import admin
from mobile.models import Telephone, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    pass

from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
import api
from api.views import UserViewSet, ProfileViewSet, TelephoneViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'telephones', TelephoneViewSet, base_name='telephones')
router.register(r'profile', ProfileViewSet, base_name='profile')

urlpatterns = patterns('',
    url(r'^$', 'mobile.views.home', name='home'),
    url(r'^api/', include(router.urls)),  # Include router urls into our urlpatterns
    url(r'^api/register/', api.views.UserRegister.as_view()),
    url(r'^api/auth/', api.views.AuthView.as_view(), name='authenticate'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^token-auth/', api.views.obtain_auth_token),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api.views import UserViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'projects', ProfileViewSet, base_name='projects')

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mobile.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

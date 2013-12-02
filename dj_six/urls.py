from __future__ import absolute_import

from django.conf.urls import patterns, include, url

from dj_six.perf.views import ItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'item', ItemViewSet)

urlpatterns = router.urls

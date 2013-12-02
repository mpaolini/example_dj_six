from __future__ import absolute_import

from rest_framework.serializers import ModelSerializer

from .models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item

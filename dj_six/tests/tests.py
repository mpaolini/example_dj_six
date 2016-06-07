from __future__ import absolute_import

from django.test import TestCase
import json

from dj_six.perf.models import Item


class ItemTestCase(TestCase):

    def test_post(self):
        resp = self.client.post('/item/',
                                json.dumps({'key': '1', 'value': 'one'}),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Item.objects.count(), 1)

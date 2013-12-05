from __future__ import absolute_import

from django.test import TestCase
import json

from .models import Item

from rest_framework.test import APITestCase

class ItemTestCase(TestCase):

    def test_post(self):
		resp = self.client.post('/item/',
			json.dumps({'key': '1', 'value': 'one'}),
			content_type='application/json')
		self.assertEqual(resp.status_code, 201)
		self.assertEqual(Item.objects.count(), 1)

class MyTests(APITestCase):

	def tests(self):
		response = self.client.post('/item/',
			json.dumps({'key': '1', 'value': 'one'}),
			content_type='application/json')
		self.assertEqual(response.status_code, 201)
		self.assertEqual(Item.objects.count(), 1)

		# response shouldn't be empty
		response = self.client.get('/item/1/')
		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(response, [])

		# update the record
		response = self.client.patch('/item/1/', {'value':'new value!'})
		self.assertEqual(response.status_code, 200)

		# after this delete there shall be no objects in the test DB
		response = self.client.delete('/item/1/')
		self.assertEqual(response.status_code, 204)
		self.assertEqual(Item.objects.count(), 0)

		# (optional) ensure the item has been removed
		response = self.client.get('/item/1/')
		self.assertEqual(response.data, {'detail':'Not found'})
from datetime import datetime

from django.core.cache import cache
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, APIClient
from unittest.mock import patch, Mock, MagicMock

from Charter.views import *


def fake_get(*args, **kwargs):
    """
    A stub urlopen() implementation that load json responses from
    the filesystem.
    """
    m = MagicMock()
    m.status_code = 200
    m.text = open('data/fixtures/example_neo_data.json', 'r').read()
    return m


class TestNeoViews(APITestCase):
    """Tests the Neo Views"""

    def setUp(self):
        self.patcher = patch('requests.get', fake_get)
        self.patcher.start()
        self.client = APIClient()
        cache.delete(datetime.now().strftime('%Y-%m-%d'))

    def get_request(self, url):
        """
        Send Get request to URL and returns results Checks status code for 200
        :param url: str, url
        :returns: response, respons.data['results']
        """
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data
        return response, results

    def test_get_data(self):
        """Test getting data for all objects"""
        response, results = self.get_request('/api/v1/nasaneo/')

        self.assertEqual(len(results), 8)
        self.assertEqual(len(results['2019-07-15']), 6)

    def test_get_estimated_diameter(self):
        """Test getting estimated diameter data"""
        response, results = self.get_request('/api/v1/neo_estimated_diameter/')

        self.assertEqual(len(results), 8)
        self.assertEqual(len(results['2019-07-15']), 6)

    def test_get_estimated_min_diameter(self):
        """Test getting estimated diameter data"""
        response, results = self.get_request('/api/v1/neo_estimated_diameter/?min=True')

        self.assertEqual(len(results), 8)
        self.assertEqual(len(results['2019-07-15']), 6)

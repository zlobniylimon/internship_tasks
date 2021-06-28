import unittest
from rest_framework.test import APIClient

import django
django.setup()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        client = APIClient()
        response = client.get('/api/moviesreviews/message/', format='json')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()

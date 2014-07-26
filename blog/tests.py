from django.core.urlresolvers import reverse
from django.test import TestCase


class BlogTest(TestCase):

    def test_status_code_equal_200(self):
        response = self.client.get(reverse('blogindex'))
        self.assertEqual(200, response.status_code)

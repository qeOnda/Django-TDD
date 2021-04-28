from django.test import TestCase
from django.urls import resolve
from .views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

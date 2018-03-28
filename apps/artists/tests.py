from __future__ import unicode_literals

from django.test import TestCase, Client
from .models import Artist, Album

# Create your tests here.
class ArtistTestCase(TestCase):
    def setUp(self): #this function does any work necessary before testing
        monk = Artist.objects.create(name="Thelonius Funk")
        Album.objects.create(title="Greatest Hits", year=1979, artist=monk)
        self.client = Client() #client is used to make http requests

    def test_index(self):
        response = self.client.get('/artists/')
        self.assertEqual("Thelonius Funk" in response.content, True)

    def test_show_page(self):
        monk = Artist.objects.get(name="Thelonius Funk")
        response = self.client.get('/artists/{}'.format(monk.id))
        self.assertEqual(response.context['artist'], monk)
        self.assertEqual("Thelonius Funk" in response.content, True)
        self.assertEqual("Greatest Hits" in response.content, True)

    def test_update(self):
        monk = Artist.objects.get(name="Thelonius Funk")
        self.client.post('/artists/{}/update'.format(monk.id), {
            "name": "Sun Ra"
        })
        sun_ra = Artist.objects.get(name="Sun Ra")
        monks = Artist.objects.filter(name="Thelonius Funk")
        self.assertEqual(sun_ra.name, "Sun Ra")
        self.assertEqual(monks.count(), 0)

"""Tests for Balloonicorn's Flask app."""

import unittest
import server


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get('/')
        self.assertIn(b'having a party', result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        # FIXME: Add a test to show we haven't RSVP'd yet
        client = server.app.test_client()
        result = client.get('/')
        self.assertIn(b'<h2>Please RSVP</h2>', result.data)
        

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': 'Jane', 'email': 'jane@jane.com'}

        result = self.client.post('/rsvp', data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        self.assertNotIn(b'<h2>Please RSVP</h2>', result.data)
        self.assertIn(b'123 Magic Unicorn Way<br>', result.data)

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself
        pass
        print('FIXME')


if __name__ == '__main__':
    unittest.main()

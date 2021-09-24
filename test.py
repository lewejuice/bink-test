import unittest
from app import app


class FlaskTestCase(unittest.TestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'The index homepage' in response.data)

    # Test current_rent function is working
    def test_current_rent(self):
        tester = app.test_client(self)
        response = tester.get('/current_rent', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Current Rent' in response.data)

    # Test lease_years function is working
    def test_lease_years(self):
        tester = app.test_client(self)
        response = tester.get('/lease_years', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Lease years' in response.data)

    # Test tenant function is working
    def test_tenant(self):
        tester = app.test_client(self)
        response = tester.get('/tenant', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Tennants' in response.data)

    # Test lease_start function is working
    def test_lease_start(self):
        tester = app.test_client(self)
        response = tester.get('/lease_start', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Lease Start Date' in response.data)


if __name__ == '__main__':
    unittest.main()
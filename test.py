import unittest
import package


class Module1TestCase(unittest.TestCase):
    def test_get_request(self):
        resp = package.module1.get_request("http://example.com")
        self.assertEqual(resp.status_code, 200, "GET request failed.")


class Module2TestCase(unittest.TestCase):
    def test_post_request(self):
        resp = package.module2.post_request("http://example.com")
        self.assertEqual(resp.status_code, 200, "POST request failed.")

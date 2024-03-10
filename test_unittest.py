from unittest import TestCase
import unittest
import requests


class MyTest(TestCase):
    def test_google(self):
        self.assertEqual(requests.get("https://google.com").status_code, 200)


if __name__ == "__main__":
    unittest.main()

from unittest import TestCase
import unittest
import requests


class Test(TestCase):
    def test(self):
        self.assertEqual(requests.get("https://google.com").status_code, 200)


if __name__ == "__main__":
    unittest.main()

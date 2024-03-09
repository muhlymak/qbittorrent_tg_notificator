from unittest import TestCase
import unittest
import requests


class Test(TestCase):
    def test_add_two_numbers(self):
        self.assertTrue(summarize(a=5, b=6) == 11, "Should be 11")

    def test(self):
        self.assertEqual(requests.get('https://google.com').status_code, 200)


if __name__ == '__main__':
    unittest.main()

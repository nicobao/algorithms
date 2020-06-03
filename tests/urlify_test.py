import unittest
from problems.arrays_strings.urlify import *


class Urlify(unittest.TestCase):

    def test_urlify(self):
        self.assertEqual((urlify('ab cd  ', 5)), 'ab%20cd')
        self.assertEqual(urlify("Mr John Smith    ", 13), "Mr%20John%20Smith")
import unittest
from problems.arrays_strings.is_unique import *

class IsUniqueTest(unittest.TestCase):
    def test_is_unique_without_set(self):
        unique_str = "qwertyuiop6;lgkd"
        non_unique_str = "foooooooulard, un vrai"

        self.assertTrue(is_unique_without_set(unique_str))
        self.assertFalse(is_unique_without_set(non_unique_str))

        self.assertTrue(is_unique_with_set(unique_str))
        self.assertFalse(is_unique_with_set(non_unique_str))

        self.assertFalse(is_unique_with_ds(non_unique_str))
        self.assertTrue(is_unique_with_ds(unique_str))


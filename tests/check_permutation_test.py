import unittest
from problems.arrays_strings.check_permutation import *

class CheckPermutationTest(unittest.TestCase):

    def test_are_permutations_sort(self):
        self.assertTrue(are_permutations_sort("qwerty", "yetrwq"))
        self.assertFalse(are_permutations_sort("yopqweyeut", "qwoiuriwtpoiwq39dkfj"))

    def test_are_permutations(self):
        self.assertTrue(are_permutations("qwerty", "yetrwq"))
        self.assertFalse(are_permutations("yopqweyeut", "qwoiuriwtpoiwq39dkfj"))

import unittest
from datastructures.hashmap import HashMap


class HashMapTest(unittest.TestCase):

    def test_put_get(self):
        hashmap = HashMap()
        # str
        hashmap.put("foo", 5)
        hashmap.put("bar", 8)
        self.assertEqual(hashmap.get("foo"), 5)
        self.assertEqual(hashmap.get("bar"), 8)

        # int
        hashmap.put(1, "value_1")
        hashmap.put(567, "value_567")
        self.assertEqual(hashmap.get("foo"), 5)
        self.assertEqual(hashmap.get("bar"), 8)
        self.assertEqual(hashmap.get(567), "value_567")
        self.assertEqual(hashmap.get(1), "value_1")

        # float
        hashmap.put(1.564, "value_1_fl")
        hashmap.put(567.9583, "value_567_fl")
        self.assertEqual(hashmap.get("foo"), 5)
        self.assertEqual(hashmap.get("bar"), 8)
        self.assertEqual(hashmap.get(567), "value_567")
        self.assertEqual(hashmap.get(1), "value_1")
        self.assertEqual(hashmap.get(567.9583), "value_567_fl")
        self.assertEqual(hashmap.get(1.564), "value_1_fl")

        # 0 < key < 1
        hashmap.put(0.564, "value_0.5")
        hashmap.put(0.9583, "value_0.9")
        self.assertEqual(hashmap.get("foo"), 5)
        self.assertEqual(hashmap.get("bar"), 8)
        self.assertEqual(hashmap.get(567), "value_567")
        self.assertEqual(hashmap.get(1), "value_1")
        self.assertEqual(hashmap.get(567.9583), "value_567_fl")
        self.assertEqual(hashmap.get(1.564), "value_1_fl")
        self.assertEqual(hashmap.get(0.9583), "value_0.9")
        self.assertEqual(hashmap.get(0.564), "value_0.5")

import unittest
from datastructures.immutable_singly_linkedlist import ImmutableSinglyLinkedList

class ImmutableSinglyLinkedListTest(unittest.TestCase):
    def test_append(self):
        immutable_singly_list = ImmutableSinglyLinkedList()
        self.assertIsNone(immutable_singly_list.value)
        self.assertIsNone(immutable_singly_list.next)
        self.assertTrue(immutable_singly_list.is_empty)
        self.assertEqual(immutable_singly_list.length, 0)

        immutable_singly_list = immutable_singly_list.append(1)
        self.assertEqual(immutable_singly_list.value, 1)
        self.assertIsNone(immutable_singly_list.next)
        self.assertEqual(immutable_singly_list.length, 1)

        immutable_singly_list = immutable_singly_list.append(2)
        self.assertEqual(immutable_singly_list.value, 1)
        self.assertIsInstance(immutable_singly_list.next, ImmutableSinglyLinkedList)
        self.assertEqual(immutable_singly_list.next.value, 2)
        self.assertIsNone(immutable_singly_list.next.next)
        self.assertEqual(immutable_singly_list.length, 2)

        immutable_singly_list = immutable_singly_list.append(3)
        self.assertEqual(immutable_singly_list.value, 1)
        self.assertIsInstance(immutable_singly_list.next, ImmutableSinglyLinkedList)
        self.assertEqual(immutable_singly_list.next.value, 2)
        self.assertIsInstance(immutable_singly_list.next.next, ImmutableSinglyLinkedList)
        self.assertEqual(immutable_singly_list.next.next.value, 3)
        self.assertIsNone(immutable_singly_list.next.next.next)
        self.assertEqual(immutable_singly_list.length, 3)

    def test_concat(self):
        immutable_singly_list = ImmutableSinglyLinkedList()
        immutable_singly_list = immutable_singly_list.concat(immutable_singly_list)
        self.assertTrue(immutable_singly_list.is_empty)

        immutable_singly_list = immutable_singly_list.append(1).append(2).append(3).append(4)
        other_list = ImmutableSinglyLinkedList().append(5).append(6).append(7)
        concat_list = immutable_singly_list.concat(other_list)

        self.assertEqual(concat_list.value, 1)
        self.assertEqual(concat_list.next.value, 2)
        self.assertEqual(concat_list.next.next.value, 3)
        self.assertEqual(concat_list.next.next.next.value, 4)
        self.assertEqual(concat_list.next.next.next.next.value, 5)
        self.assertEqual(concat_list.next.next.next.next.next.value, 6)
        self.assertEqual(concat_list.next.next.next.next.next.next.value, 7)
        self.assertIsNone(concat_list.next.next.next.next.next.next.next)
        self.assertEqual(concat_list.length, 7)

    def test_insert(self):
        immutable_singly_list = ImmutableSinglyLinkedList()
        immutable_singly_list = immutable_singly_list.insert(1, 2)
        self.assertTrue(immutable_singly_list.is_empty)

        append_1 = immutable_singly_list.append(1)
        immutable_singly_list = append_1.insert(2, 3)
        self.assertEqual(append_1, immutable_singly_list)

        immutable_singly_list = immutable_singly_list.insert(2, 1)
        self.assertEqual(immutable_singly_list, ImmutableSinglyLinkedList(1).append(2))

        immutable_singly_list = immutable_singly_list.insert(3, 1)
        self.assertEqual(immutable_singly_list, ImmutableSinglyLinkedList(1).append(3).append(2))

        immutable_singly_list = immutable_singly_list.insert(4, 3)
        self.assertEqual(immutable_singly_list, ImmutableSinglyLinkedList(1).append(3).append(4).append(2))




if __name__ == "__main__":
    unittest.main()
import unittest
from datastructures.tree import BinaryTree, Node, traverse_preorder

class BinaryTreeTest(unittest.TestCase):
    def test_add(self):

        binary_tree = BinaryTree(1)
        node = Node(1)
        self.assertEqual(binary_tree.root, node)

        binary_tree.add_left(2)
        node.left = Node(2)
        self.assertEqual(binary_tree.root, node)

        binary_tree.add_right(3)
        node.right = Node(3)
        self.assertEqual(binary_tree.root, node)

        binary_tree.add_left(1)
        node.left.left = Node(1)
        self.assertEqual(binary_tree.root, node)

        binary_tree.add_left(4)
        node.left.left.left = Node(4)
        self.assertEqual(binary_tree.root, node)

        binary_tree.add_right(5).add_left(7)
        node.right.right = Node(5)
        node.right.right.left = Node(7)
        print(node)
        print(binary_tree)
        self.assertEqual(binary_tree.root, node)

class TraverseTest(unittest.TestCase):
    pass
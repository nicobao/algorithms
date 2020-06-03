import unittest
from datastructures.graph import *
from collections import deque


class GraphTest(unittest.TestCase):
    def test_dfs_adjacency_list(self):
        adjacency_list = [[1], [2], [0, 3], [2], [6], [4], [5]]

        order_visited = deque([0, 1, 2, 3])
        order_visited_from_4 = deque([4, 6, 5])

        self.assertEqual(dfs_adjacency_list(adjacency_list), order_visited)
        self.assertEqual(dfs_adjacency_list(adjacency_list, 4), order_visited_from_4)

        with self.assertRaises(ValueError):
            dfs_adjacency_list(adjacency_list, -1)
            dfs_adjacency_list(adjacency_list, len(adjacency_list))
            dfs_adjacency_list(adjacency_list, len(adjacency_list) + 10)


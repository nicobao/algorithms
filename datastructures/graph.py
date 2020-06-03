from collections import deque


def dfs_adjacency_list(adjacency_list: list, start: int = 0) -> 'deque':
    return _dfs_adjacency_list(adjacency_list, start, deque([]))


def _dfs_adjacency_list(adjacency_list: list, start: int, visited: 'deque') -> 'deque':
    """
    adjacency_list is a list of list
    [[1, 2], [0, 2]...etc]
    Return the queue of nodes in the order we have visited them
    """
    if start < 0 or start >= len(adjacency_list):
        raise ValueError("Start index must be within adjacency list length")
    visited.append(start)
    children = adjacency_list[start]
    if children:
        for child in children:
            if child not in visited:
                _dfs_adjacency_list(adjacency_list, child, visited)
    return visited

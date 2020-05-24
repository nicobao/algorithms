from typing import Union, Generator

class Node:
    def __init__(self, value: int):
        self._value = value
        self._left = None
        self._right = None

    @property
    def left(self) -> "Node":
        return self._left

    @property
    def right(self) -> "Node":
        return self._right

    @property
    def value(self) -> int:
        return self._value

    @right.setter
    def right(self, node: "Node") -> None:
        self._right = node

    @left.setter
    def left(self, node: "Node") -> None:
        self._left = node

    def __repr__(self):
        return '(value: {value}, left: {left}, right: {right})'.format(value = self._value,
                                                                      left = self._left,
                                                                      right = self._right)

    def __eq__(self, other_node: "Node") -> bool:
        if other_node is None:
            return False

        if self._value != other_node.value:
            return False

        if (self._left is None and other_node.left is not None) or \
                (self._left is not None and other_node.left is None) or \
                (self._right is None and other_node.right is not None) or \
                (self._right is not None and other_node.right is None):
            return False
        # At this point, self and other node "right" are either both None or none of them are None. Same for their left.
        elif self._left is None and other_node.left is None:
            if self._right is None and other_node.right is None:
                # We got until the end of the tree, and all values were equal
                return True
            else:
                # This call is recursive
                return self._right == other_node.right
        elif self._right is None and other_node.right is None:
            # This call is recursive
            return self._left == other_node.left
        else:
            # This call is recursive
            return self._left == other_node.left and self._right == other_node.right

class BinaryTree:
    def __init__(self, root_value : int):
        self._root = Node(root_value)

    @property
    def root(self) -> "Node":
        return self._root

    def add_left(self, value: int) -> "BinaryTree":
        return self._add_side(value, 'left')


    def add_right(self, value: int) -> "BinaryTree":
        return self._add_side(value, 'right')

    def _add_side(self, value: int, side: str) -> "BinaryTree":
        current_node = self._root
        while (getattr(current_node, side) is not None):
            current_node = getattr(current_node, side)
        setattr(current_node, side, Node(value))
        return self  # so you can pipe add operations

        # current_node = self._root
        # while current_node is not None:
        #     yield current_node.value
        #     current_node = current_node.left
        # current_node = self._root.right
        # while current_node is not None:
        #     yield current_node.value
        #     current_node = current_node.right

    def __repr__(self):
        return '\n{}'.format(self._root)


def traverse_preorder(tree_or_node: Union["BinaryTree", "Node"]) -> Generator[int, None, None]:
    if isinstance(tree_or_node, BinaryTree):
        traverse_preorder(tree_or_node.root)
    elif isinstance(tree_or_node, Node):
        yield tree_or_node.value
        if tree_or_node.left is not None:
            traverse_preorder(tree_or_node.left)
        elif tree_or_node.right is not None:
            traverse_preorder(tree_or_node.right)
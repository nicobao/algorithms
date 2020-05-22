class Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    @left.setter
    def left(self, node):
        self._left = node

    def __repr__(self):
        return '(value: {value}, left: {left}, right: {right})'.format(value = self._value,
                                                                      left = self._left,
                                                                      right = self._right)

class BinaryTree:
    def __init__(self, root_value):
        self._root = Node(root_value)

    def add_left(self, value):
        self._add_side(value, 'left')

    def add_right(self, value):
        self._add_side(value, 'right')

    def _add_side(self, value, side):
        current_node = self._root
        while (getattr(current_node, side) is not None):
            current_node = getattr(current_node, side)
        setattr(current_node, side, Node(value))

    def __repr__(self):
        return '\n{}'.format(self._root)

if __name__ == '__main__':
    binary_tree = BinaryTree(1)
    print(binary_tree)
    binary_tree.add_left(2)
    print(binary_tree)
    binary_tree.add_right(3)
    print(binary_tree)
    binary_tree.add_left(1)
    print(binary_tree)
    binary_tree.add_left(4)
    print(binary_tree)
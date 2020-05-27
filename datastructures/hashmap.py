from math import trunc


class HashMap:

    def __init__(self):
        self._length = 16384
        self._array_list = [None for _ in range(self._length)]

    def get(self, key):
        hash_value = self._hash(key)
        index_list = self._hash_to_index(hash_value)
        linked_list = self._array_list[index_list]
        if not linked_list:
            return None
        else:
            for node in linked_list:
                if node.key == key:
                    return node.value

    def put(self, key, value):
        if self._array_list[self._length - 1]:
            self._increase_list_size()
            # This should be done internally in the ArrayList datastructure,
            # when attempting to add value to index >= self._length
        hash_value = self._hash(key)
        index_list = self._hash_to_index(hash_value)
        linked_list = self._array_list[index_list]
        if not linked_list:
            self._array_list[index_list] = [Node(key, value)]  # this should normally be a linked list...
        else:
            already_existing = False
            for node in linked_list:
                new_node = Node(key, value)
                if node == new_node:
                    node.value = new_node.value
                    already_existing = True
                    break
            if not already_existing:
                linked_list.append(Node(key, value))

    def _hash(self, key):
        if isinstance(key, int):
            return self._hash_int(key)
        if isinstance(key, float):
            if key.is_integer():
                return self._hash_int(key)
            else:
                return self._hash_float(key)
        if isinstance(key, str):
            return self._hash_str(key)

    def _hash_int(self, key):
        return key % self._length

    def _hash_float(self, key):
        if abs(key) > 0 and abs(key) < 1:
            # The value below is defective because it gives more weight
            # to the most significant bits of the keys.
            # The least significant bits play no role.
            # One way to address this situation is to use modular hashing on the binary
            # representation of the key.
            # see https://algs4.cs.princeton.edu/34hash/
            return trunc(abs(key)*self._length)
        return trunc(abs(key)) % self._length

    def _hash_str(self, key):
        hash = 0
        small_prime_int = 31
        for char in key:
            hash = (small_prime_int * hash + ord(char)) % self._length
        return hash

    def _hash_to_index(self, hash_value):
        return hash_value % (self._length - 1)

    def _increase_list_size(self):
        # O(size old list)
        self._length = self._length*2
        new_list = [None for _ in range(1, self._length)]
        for index, node in enumerate(self._array_list):
            new_list[index] = self._array_list[index]
        self._array_list = new_list


class Node:
    def __init__(self, key, value):
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __eq__(self, other):
        return self._key == other.key

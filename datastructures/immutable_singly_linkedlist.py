class ImmutableSinglyLinkedList:
    """
    A persistent singly linked list
    """
    def __init__(self, value: int = None, next: "ImmutableSinglyLinkedList" = None):
        self._value = value
        self._next = next

    @property
    def is_empty(self):
        return self._value is None and self._next is None

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @property
    def length(self):
        if self.is_empty:
            return 0
        current_node = self
        counter = 1
        while current_node.next is not None:
            counter = counter + 1
            current_node = current_node.next
        return counter

    def append(self, new_value: int) -> "ImmutableSinglyLinkedList":
        if self.is_empty:
            return ImmutableSinglyLinkedList(new_value)
        if self._next is None:
            return ImmutableSinglyLinkedList(self._value, ImmutableSinglyLinkedList(new_value))
        return ImmutableSinglyLinkedList(self._value, self._next.append(new_value))

    def concat(self, other_list: "ImmutableSinglyLinkedList") -> "ImmutableSinglyLinkedList":
        if other_list is None:
            return self
        list_to_return = self
        if not other_list.is_empty:
            list_to_return = list_to_return.append(other_list.value)
        current_other_node = other_list
        while current_other_node.next is not None:
            current_other_node = current_other_node.next
            list_to_return = list_to_return.append(current_other_node.value)
        return list_to_return

    def insert(self, new_value: int, after_first_value: int) -> "ImmutableSinglyLinkedList":
        """
        Insert "new_value right after the first occurence of "after_first_value found in the list,
        and return the newly formed list.
        If no occurence is found, return the original list.
        """
        if self._next is None:
            if self._value == after_first_value:
                return ImmutableSinglyLinkedList(self._value, ImmutableSinglyLinkedList(new_value))
            return self
        first_value_node = self
        full_list_to_first_value_node = ImmutableSinglyLinkedList()
        while first_value_node.value != after_first_value and first_value_node.next is not None:
            full_list_to_first_value_node = full_list_to_first_value_node.append(first_value_node.value)
            first_value_node = first_value_node.next
        if first_value_node.value != after_first_value:
            # Happens when reaching the end of the list without finding the value
            return self
        appended_first_value_node = full_list_to_first_value_node.append(after_first_value).append(new_value)
        return appended_first_value_node.concat(first_value_node.next)

    def __repr__(self):
        return "value: {value}\nnext:{next}".format(value=self._value,
                                                    next=self._next)

    def __eq__(self, other: "ImmutableSinglyLinkedList") -> bool:
        if other.length != self.length:
            return False
        return self._value == other.value and self._next == other.next





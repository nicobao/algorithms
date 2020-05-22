class Node:
    def __init__(self, dataval=None):
        self._dataval = dataval
        self._nextval = None

    @property
    def nextval(self):
        return self._nextval

    @property
    def dataval(self):
        return self._dataval

    @nextval.setter
    def nextval(self, nextval):
        self._nextval = nextval

    def __repr__(self):
        if self._nextval is None:
            return '(dataval: {dataval}, nextval: {nextval})'.format(dataval = self._dataval,
                                       nextval = self._nextval)
        return '(dataval: {dataval}, nextval:\n{nextval})'.format(dataval = self._dataval,
                                          nextval = self._nextval)

class SingleLinkedList:
    """
    A simply linked list, non immutable
    """
    def __init__(self, head=None):
        self._head = Node(head)

    def insert_begin(self, data):
        new_head = Node(data)
        new_head.nextval = self._head
        self._head = new_head

    def insert_end(self, data):
        current_node = self._head
        while (current_node.nextval != None):
            current_node = current_node.nextval
        current_node.nextval = Node(data)

    def insert_after(self, data, existing_value):
        if self._head.dataval == existing_value:
            self._do_insert_after(data, self._head)
            return
        current_node = self._head
        while existing_value != current_node.dataval:
            current_node = current_node.nextval
        self._do_insert_after(data, current_node)

    def _do_insert_after(self, data, existing_node: "Node"):
        new_node = Node(data)
        new_node.nextval = existing_node.nextval
        existing_node.nextval = new_node

    def length(self) -> int:
        counter = 0
        while (self._head.nextval is not None):
            counter+= counter
        return counter

    # def delete(self, ):

    def __repr__(self):
        to_return = '\n{}'.format(self._head)
        # current_node = self._head
        # while current_node is not None:
        #     to_return.join('current_node: {}\n'.format(current_node.__repr__))
        return to_return

if __name__ == '__main__':
    linked_list = SingleLinkedList(0)
    print(linked_list)
    linked_list.insert_begin(1)
    print(linked_list)
    linked_list.insert_begin(5)
    print(linked_list)
    linked_list.insert_end(3)
    print(linked_list)
    linked_list.insert_after(4, 0)
    print(linked_list)


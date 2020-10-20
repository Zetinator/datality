from typing import Any, List, Optional
from datality.double_linked_list import DoubleLinkedList


class Node:
    """node chainable storage unit"""

    def __init__(self, value: Any = None):
        self.value: Any = value
        self.next: Optional[Node] = None


class Deque(DoubleLinkedList):
    """implementation of a double ended queue

    https://en.wikipedia.org/wiki/Double-ended_queue
    """

    def __init__(self, values: List[Any] = []):
        super().__init__(values)

    def append_left(self, value: Any) -> None:
        """append a new node to the head of the list

        Args:
            value (Any): value to append, in a new node
        """
        # empty list
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
            return
        # general case
        tmp = self.head
        self.head = Node(value)
        self.head.next = tmp
        # update length
        self.length += 1

    def pop_left(self) -> Any:
        """pop the element at the begining of the list

        Returns:
            Any: the element at the begining of the list
        """
        # special case: empty list
        if not self.head:
            raise IndexError()
        tmp = self.head
        # special case: single item
        if self.head == self.tail:
            self.tail = self.head.next
        self.head = self.head.next
        return tmp

    def pop_right(self) -> Any:
        """pop the element at the end of the list

        Returns:
            Any: the element at the end of the list
        """
        # special case: empty list
        if not self.head:
            raise IndexError()
        tmp = self.tail
        # special case: single item
        if self.head == self.tail:
            self.head = None
        self.tail = self.tail.prev
        return tmp

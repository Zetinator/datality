"""custom implementation of a stack with the purpose of practice
the ADT contains the following methods:
    - push
    - pop
    - peek
"""


class Stack:
    class Node:
        """Node basic chainable storage unit"""

        def __init__(self, x=None):
            self.value = x
            self.next = None

    def __init__(self, x=[]):
        self.head = None
        for e in x:
            self.push(e)

    def push(self, x):
        """push a new node into the stack"""
        # special case: empty stack
        if not self.head:
            self.head = self.Node(x)
            return
        # general case
        tmp = self.head
        self.head = self.Node(x)
        self.head.next = tmp
        return

    def peek(self):
        """peek the top node of the stack"""
        return self.head

    def pop(self):
        """pop the top node of the stack"""
        # special case: empty list
        if not self.head:
            return
        # general case
        tmp = self.head
        self.head = self.head.next
        return tmp

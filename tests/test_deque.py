import pytest
from datality.deque import Deque


def test_linked_list_append():
    """create a linked list from a list of values"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    dq = Deque(init)
    assert len(dq) == 20
    # empty list
    init = []
    dq = Deque(init)
    assert not dq
    # list of words
    init = ["erick", "sophia", "marion"]
    dq = Deque(init)
    assert len(dq) == 3


def test_linked_list_search():
    """search in a linked list for a given value"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    dq = Deque(init)
    assert dq.search(3).value == 3
    # empty list
    init = []
    dq = Deque(init)
    with pytest.raises(ValueError):
        dq.search(3)
    # list of words
    init = ["erick", "sophia", "marion"]
    dq = Deque(init)
    assert dq.search("sophia").value == "sophia"


def test_linked_list_insert():
    """inserts a new node with the given `value` at the `index` position"""
    # empty list
    init = []
    dq = Deque(init)
    dq.insert("marion", 10)
    assert len(dq) == 1
    assert dq.head == dq.tail
    assert dq.head.value == "marion"
    # just one node insert at 0
    init = [7]
    dq = Deque(init)
    dq.insert(69, 0) == 3
    assert len(dq) == 2
    assert dq.head.value == 69
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    dq = Deque(init)
    dq.insert(69, 3)
    assert len(dq) == 21
    assert dq.head.next.next.next.value == 69


def test_linked_list_delete():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    dq = Deque(init)
    with pytest.raises(ValueError):
        dq.delete("marion")
    # value not found
    init = [7]
    dq = Deque(init)
    with pytest.raises(ValueError):
        dq.delete(8)
    # single item
    init = [7]
    dq = Deque(init)
    dq.delete(7)
    assert not dq
    assert dq.head == dq.tail
    assert dq.head is None
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    dq = Deque(init)
    dq.delete(15)
    assert len(dq) == 19
    assert dq.head.next.next.value == 3
    # delete tail
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    dq = Deque(init)
    dq.delete(16)
    assert len(dq) == 19
    assert dq.tail.value == 16
    assert dq.tail.next is None


def test_linked_list_getitem():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    dq = Deque(init)
    with pytest.raises(IndexError):
        dq[1]
    # single item
    init = [7]
    dq = Deque(init)
    assert dq[0].value == 7
    with pytest.raises(IndexError):
        dq[2]
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    dq = Deque(init)
    assert dq[2].value == 15
    assert dq[-1].value == 16


def test_deque_pop_left():
    """pops node from the left"""
    # empty list
    init = []
    dq = Deque(init)
    with pytest.raises(IndexError):
        dq.pop_left()
    # single item
    init = [7]
    dq = Deque(init)
    assert dq.pop_left().value == 7
    assert dq.head == dq.tail
    assert dq.head is None
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    dq = Deque(init)
    for i in range(len(dq)):
        assert dq.pop_left().value == init[i]


def test_deque_pop_right():
    """pops node from the right"""
    # empty list
    init = []
    dq = Deque(init)
    with pytest.raises(IndexError):
        dq.pop_right()
    # single item
    init = [7]
    dq = Deque(init)
    assert dq.pop_right().value == 7
    assert dq.head == dq.tail
    assert dq.head is None
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    dq = Deque(init)
    for i in range(len(dq)):
        assert dq.pop_right().value == init[-i - 1]


def test_deque_append_left():
    """appends node from the left"""
    # empty list
    init = []
    dq = Deque(init)
    dq.append_left(69)
    assert dq[0].value == 69
    # single item
    init = [7]
    dq = Deque(init)
    dq.append_left(69)
    assert dq[0].value == 69
    assert dq.head.value == 69
    assert dq.tail.value == 7
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    dq = Deque()
    for e in init:
        dq.append_left(e)
    for i in range(len(dq)):
        assert dq.pop_left().value == init[-i - 1]

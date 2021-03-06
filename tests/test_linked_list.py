import pytest

from datality.linked_list import LinkedList


def test_linked_list_append():
    """create a linked list from a list of values"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    ll = LinkedList(init)
    assert len(ll) == 20
    # empty list
    init = []
    ll = LinkedList(init)
    assert not ll
    # list of words
    init = ["erick", "sophia", "marion"]
    ll = LinkedList(init)
    assert len(ll) == 3


def test_linked_list_search():
    """search in a linked list for a given value"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    ll = LinkedList(init)
    assert ll.search(3).value == 3
    # empty list
    init = []
    ll = LinkedList(init)
    with pytest.raises(ValueError):
        ll.search(3)
    # list of words
    init = ["erick", "sophia", "marion"]
    ll = LinkedList(init)
    assert ll.search("sophia").value == "sophia"
    with pytest.raises(ValueError):
        ll.search("kim")


def test_linked_list_insert():
    """inserts a new node with the given `value` at the `index` position"""
    # empty list
    init = []
    ll = LinkedList(init)
    ll.insert("marion", 10)
    assert len(ll) == 1
    assert ll.head == ll.tail
    assert ll.head.value == "marion"
    # just one node insert at 0
    init = [7]
    ll = LinkedList(init)
    ll.insert(69, 0) == 3
    assert len(ll) == 2
    assert ll.head.value == 69
    # insert at tail
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    ll = LinkedList(init)
    ll.insert(69, -1)
    assert len(ll) == 21
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    ll = LinkedList(init)
    ll.insert(69, 3)
    assert len(ll) == 21
    assert ll.head.next.next.next.value == 69


def test_linked_list_delete():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    ll = LinkedList(init)
    with pytest.raises(ValueError):
        ll.delete("marion")
    # value not found
    init = [7]
    ll = LinkedList(init)
    with pytest.raises(ValueError):
        ll.delete(8)
    ll.delete(7)
    assert len(ll) == 0
    # delete tail
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    ll = LinkedList(init)
    ll.delete(16)
    assert len(ll) == 19
    assert ll.tail.value == 16
    assert ll.tail.next is None
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    ll = LinkedList(init)
    for e in range(20):
        ll.delete(e)


def test_linked_list_getitem():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    ll = LinkedList(init)
    with pytest.raises(IndexError):
        ll[1]
    # value not found
    init = [7]
    ll = LinkedList(init)
    assert ll[0].value == 7
    with pytest.raises(IndexError):
        ll[2]
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    ll = LinkedList(init)
    assert ll[2].value == 15
    assert ll[-1].value == 16


def test_linked_list_repr():
    """deletes a new node with the given `value`"""
    # empty
    init = []
    ll = LinkedList(init)
    # single
    init = [7]
    ll = LinkedList(init)
    res = """7"""
    assert repr(ll) == res
    # repeated
    init = [7, 7, 7, 7, 7, 7, 7]
    ll = LinkedList(init)
    res = """7 -> 7 -> 7 -> 7 -> 7 -> 7 -> 7"""
    assert repr(ll) == res
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    ll = LinkedList(init)
    res = """7 -> 17 -> 15 -> 3 -> 8 -> 13 -> 1 -> 18 -> 19 -> 0 -> 12 -> 5 -> 10 -> 9 -> 4 -> 14 -> 11 -> 2 -> 6 -> 16"""
    assert repr(ll) == res

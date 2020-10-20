import pytest
from collectionz.linked_list import LinkedList


def test_linked_list_append():
    """create a linked list from a list of values"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
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
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
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
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
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
    # single item
    init = [7]
    ll = LinkedList(init)
    ll.delete(7)
    assert not ll
    assert ll.head == ll.tail
    assert ll.head is None
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    ll = LinkedList(init)
    ll.delete(15)
    assert len(ll) == 19
    assert ll.head.next.next.value == 3
    # delete tail
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    ll = LinkedList(init)
    ll.delete(16)
    assert len(ll) == 19
    assert ll.tail.value == 16
    assert ll.tail.next is None


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
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    ll = LinkedList(init)
    assert ll[2].value == 15
    assert ll[-1].value == 16

import pytest
from datality.treap import Treap


def test_avl_initialize():
    """create a treap from a list of values"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    treap = Treap(init)
    assert len(treap) == 20
    # empty list
    init = []
    treap = Treap(init)
    assert not treap
    # list of words
    init = ["erick", "sophia", "marion"]
    treap = Treap(init)
    assert len(treap) == 3


def test_avl_search():
    """search in the treap the given value"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    treap = Treap(init)
    assert treap.search(3).value == 3
    # empty list
    init = []
    treap = Treap(init)
    with pytest.raises(KeyError):
        treap.search(3)
    # list of words
    init = ["erick", "sophia", "marion"]
    treap = Treap(init)
    assert treap.search("sophia").value == "sophia"


def test_avl_delete():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    treap = Treap(init)
    with pytest.raises(KeyError):
        treap.delete("marion")
    # value not found
    init = [7]
    treap = Treap(init)
    with pytest.raises(KeyError):
        treap.delete(8)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    treap = Treap(init)
    treap.delete(15)
    assert len(treap) == 19
    with pytest.raises(KeyError):
        treap.search(15)
    # delete head
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    treap = Treap(init)
    head_value = treap.root.value
    treap.delete(head_value)
    assert len(treap) == 19
    with pytest.raises(KeyError):
        assert treap.search(head_value)


def test_avl_successor():
    """get the successor of the given value"""
    # empty list
    init = []
    treap = Treap(init)
    with pytest.raises(KeyError):
        treap.successor(5)
    # value not found
    init = [7]
    treap = Treap(init)
    with pytest.raises(KeyError):
        treap.successor(8)
    # no successor on the tree
    init = [7]
    treap = Treap(init)
    with pytest.raises(KeyError):
        treap.successor(7)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    treap = Treap(init)
    assert treap.successor(0).value == 1
    assert treap.successor(7).value == 8
    assert treap.successor(17).value == 18

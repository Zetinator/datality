import pytest
from collectionz.rb_tree import RBTree


def test_rb_tree_initialize():
    """create a rb_tree from a list of values"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    rb = RBTree(init)
    assert len(rb) == 20
    # empty list
    init = []
    rb = RBTree(init)
    assert not rb
    # list of words
    init = ["erick", "sophia", "marion"]
    rb = RBTree(init)
    assert len(rb) == 3


def test_rb_tree_search():
    """search in the rb the given value"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    rb = RBTree(init)
    assert rb.search(3).value == 3
    # empty list
    init = []
    rb = RBTree(init)
    with pytest.raises(KeyError):
        rb.search(3)
    # list of words
    init = ["erick", "sophia", "marion"]
    rb = RBTree(init)
    assert rb.search("sophia").value == "sophia"


def test_rb_tree_delete():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    rb = RBTree(init)
    with pytest.raises(KeyError):
        rb.delete("marion")
    # value not found
    init = [7]
    rb = RBTree(init)
    with pytest.raises(KeyError):
        rb.delete(8)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    rb = RBTree(init)
    rb.delete(15)
    assert len(rb) == 19
    with pytest.raises(KeyError):
        rb.search(15)
    # delete head
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    rb = RBTree(init)
    head_value = rb.root.value
    rb.delete(head_value)
    assert len(rb) == 19
    with pytest.raises(KeyError):
        assert rb.search(head_value)


def test_rb_tree_successor():
    """get the successor of the given value"""
    # empty list
    init = []
    rb = RBTree(init)
    with pytest.raises(KeyError):
        rb.successor(5)
    # value not found
    init = [7]
    rb = RBTree(init)
    with pytest.raises(KeyError):
        rb.successor(8)
    # no successor on the tree
    init = [7]
    rb = RBTree(init)
    with pytest.raises(KeyError):
        rb.successor(7)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    rb = RBTree(init)
    assert rb.successor(0).value == 1
    assert rb.successor(7).value == 8
    assert rb.successor(17).value == 18

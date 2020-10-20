import pytest
from datality.splay_tree import SplayTree


def test_avl_initialize():
    """create a splay_tree from a list of values"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    splay_tree = SplayTree(init)
    assert len(splay_tree) == 20
    # empty list
    init = []
    splay_tree = SplayTree(init)
    assert not splay_tree
    # list of words
    init = ["erick", "sophia", "marion"]
    splay_tree = SplayTree(init)
    assert len(splay_tree) == 3


def test_avl_search():
    """search in the splay_tree the given value"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    splay_tree = SplayTree(init)
    assert splay_tree.search(3).value == 3
    # empty list
    init = []
    splay_tree = SplayTree(init)
    with pytest.raises(KeyError):
        splay_tree.search(3)
    # list of words
    init = ["erick", "sophia", "marion"]
    splay_tree = SplayTree(init)
    assert splay_tree.search("sophia").value == "sophia"


def test_avl_delete():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    splay_tree = SplayTree(init)
    with pytest.raises(KeyError):
        splay_tree.delete("marion")
    # value not found
    init = [7]
    splay_tree = SplayTree(init)
    with pytest.raises(KeyError):
        splay_tree.delete(8)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    splay_tree = SplayTree(init)
    splay_tree.delete(15)
    assert len(splay_tree) == 19
    with pytest.raises(KeyError):
        splay_tree.search(15)
    # delete head
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    splay_tree = SplayTree(init)
    head_value = splay_tree.root.value
    splay_tree.delete(head_value)
    assert len(splay_tree) == 19
    with pytest.raises(KeyError):
        assert splay_tree.search(head_value)


def test_avl_successor():
    """get the successor of the given value"""
    # empty list
    init = []
    splay_tree = SplayTree(init)
    with pytest.raises(KeyError):
        splay_tree.successor(5)
    # value not found
    init = [7]
    splay_tree = SplayTree(init)
    with pytest.raises(KeyError):
        splay_tree.successor(8)
    # no successor on the tree
    init = [7]
    splay_tree = SplayTree(init)
    with pytest.raises(KeyError):
        splay_tree.successor(7)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19,
            0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    splay_tree = SplayTree(init)
    assert splay_tree.successor(0).value == 1
    assert splay_tree.successor(7).value == 8
    assert splay_tree.successor(17).value == 18

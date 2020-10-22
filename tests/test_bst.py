import pytest

from datality.bst import BST


def test_bst_initialize():
    """create a bst from a list of values"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    bst = BST(init)
    assert len(bst) == 20
    # empty list
    init = []
    bst = BST(init)
    assert not bst
    # list of words
    init = ["erick", "sophia", "marion"]
    bst = BST(init)
    assert len(bst) == 3


def test_bst_search():
    """search in the bst the given value"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    bst = BST(init)
    assert bst.search(3).value == 3
    # empty list
    init = []
    bst = BST(init)
    with pytest.raises(KeyError):
        bst.search(3)
    # list of words
    init = ["erick", "sophia", "marion"]
    bst = BST(init)
    assert bst.search("sophia").value == "sophia"


def test_bst_delete():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    bst = BST(init)
    with pytest.raises(KeyError):
        bst.delete("marion")
    # value not found
    init = [7]
    bst = BST(init)
    with pytest.raises(KeyError):
        bst.delete(8)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    bst = BST(init)
    bst.delete(15)
    assert len(bst) == 19
    with pytest.raises(KeyError):
        bst.search(15)
    # delete head
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    bst = BST(init)
    bst.delete(7)
    assert len(bst) == 19
    assert bst.root.value == 3


def test_bst_successor():
    """get the successor of the given value"""
    # empty list
    init = []
    bst = BST(init)
    with pytest.raises(KeyError):
        bst.successor(5)
    # value not found
    init = [7]
    bst = BST(init)
    with pytest.raises(KeyError):
        bst.successor(8)
    # no successor on the tree
    init = [7]
    bst = BST(init)
    with pytest.raises(KeyError):
        bst.successor(7)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    bst = BST(init)
    assert bst.successor(0).value == 1
    assert bst.successor(7).value == 8
    assert bst.successor(17).value == 18

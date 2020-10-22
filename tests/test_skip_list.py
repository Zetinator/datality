import pytest

from datality.skip_list import SkipList


def test_bst_initialize():
    """create a skip_list from a list of values"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    skip_list = SkipList(init)
    assert len(skip_list) == 20
    # empty list
    init = []
    skip_list = SkipList(init)
    assert not skip_list
    # list of words
    init = ["erick", "sophia", "marion"]
    skip_list = SkipList(init)
    assert len(skip_list) == 3


def test_bst_search():
    """search in the skip_list the given value"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    skip_list = SkipList(init)
    assert skip_list.search(3).value == 3
    # empty list
    init = []
    skip_list = SkipList(init)
    with pytest.raises(KeyError):
        skip_list.search(3)
    # list of words
    init = ["erick", "sophia", "marion"]
    skip_list = SkipList(init)
    assert skip_list.search("sophia").value == "sophia"


def test_bst_delete():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    skip_list = SkipList(init)
    with pytest.raises(KeyError):
        skip_list.delete("marion")
    # value not found
    init = [7]
    skip_list = SkipList(init)
    with pytest.raises(KeyError):
        skip_list.delete(8)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    skip_list = SkipList(init)
    skip_list.delete(15)
    assert len(skip_list) == 19
    with pytest.raises(KeyError):
        skip_list.search(15)
    # delete head
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    skip_list = SkipList(init)
    skip_list.delete(7)
    assert len(skip_list) == 19
    with pytest.raises(KeyError):
        skip_list.search(7)


def test_bst_successor():
    """get the successor of the given value"""
    # empty list
    init = []
    skip_list = SkipList(init)
    with pytest.raises(KeyError):
        skip_list.successor(5)
    # value not found
    init = [7]
    skip_list = SkipList(init)
    with pytest.raises(KeyError):
        skip_list.successor(8)
    # no successor on the tree
    init = [7]
    skip_list = SkipList(init)
    with pytest.raises(KeyError):
        skip_list.successor(7)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    skip_list = SkipList(init)
    assert skip_list.successor(0).value == 1
    assert skip_list.successor(7).value == 8
    assert skip_list.successor(17).value == 18
    assert skip_list.successor(18).value == 19
    with pytest.raises(KeyError):
        skip_list.successor(19)

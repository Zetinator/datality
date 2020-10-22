import pytest

from datality.avl import AVL


def test_avl_initialize():
    """create a avl from a list of values"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    avl = AVL(init)
    print(f'\n{avl}')
    assert len(avl) == 20
    # empty list
    init = []
    avl = AVL(init)
    assert not avl
    # list of words
    init = ["erick", "sophia", "marion"]
    avl = AVL(init)
    assert len(avl) == 3


def test_avl_search():
    """search in the avl the given value"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    avl = AVL(init)
    assert avl.search(3).value == 3
    # empty list
    init = []
    avl = AVL(init)
    with pytest.raises(KeyError):
        avl.search(3)
    # list of words
    init = ["erick", "sophia", "marion"]
    avl = AVL(init)
    assert avl.search("sophia").value == "sophia"


def test_avl_delete():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    avl = AVL(init)
    with pytest.raises(KeyError):
        avl.delete("marion")
    # value not found
    init = [7]
    avl = AVL(init)
    with pytest.raises(KeyError):
        avl.delete(8)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    avl = AVL(init)
    avl.delete(15)
    assert len(avl) == 19
    with pytest.raises(KeyError):
        avl.search(15)
    # delete head
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    avl = AVL(init)
    head_value = avl.root.value
    avl.delete(head_value)
    assert len(avl) == 19
    with pytest.raises(KeyError):
        assert avl.search(head_value)


def test_avl_successor():
    """get the successor of the given value"""
    # empty list
    init = []
    avl = AVL(init)
    with pytest.raises(KeyError):
        avl.successor(5)
    # value not found
    init = [7]
    avl = AVL(init)
    with pytest.raises(KeyError):
        avl.successor(8)
    # no successor on the tree
    init = [7]
    avl = AVL(init)
    with pytest.raises(KeyError):
        avl.successor(7)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    avl = AVL(init)
    assert avl.successor(0).value == 1
    assert avl.successor(7).value == 8
    assert avl.successor(17).value == 18

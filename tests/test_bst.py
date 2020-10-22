import pytest

from datality.bst import BST


def test_bst_initialize():
    """create a bst from a list of values"""
    # empty list
    init = []
    bst = BST(init)
    assert not bst
    # single
    init = [7]
    bst = BST(init)
    assert len(bst) == 1
    # repeated
    init = [7, 10, 7]
    bst = BST(init)
    assert len(bst) == 2
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    bst = BST(init)
    assert len(bst) == 20
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
    for e in init:
        bst.delete(e)
    assert len(bst) == 0
    # erase non exitent
    with pytest.raises(KeyError):
        bst.search(15)
    # delete head
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    bst = BST(init)
    head_value = bst.root.value
    bst.delete(head_value)
    assert len(bst) == 19
    with pytest.raises(KeyError):
        assert bst.search(head_value)


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
    for e in range(19):
        bst.successor(e) == e + 1
    with pytest.raises(KeyError):
        bst.successor(19)


def test_bst_repr():
    """get the repr"""
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    bst = BST(init)
    res = """			-->(19)
		-->(18)
	-->(17)
			-->(16)
		-->(15)
					-->(14)
				-->(13)
					-->(12)
							-->(11)
						-->(10)
							-->(9)
			-->(8)
-->(7)
			-->(6)
		-->(5)
			-->(4)
	-->(3)
			-->(2)
		-->(1)
			-->(0)"""
    assert repr(bst) == res

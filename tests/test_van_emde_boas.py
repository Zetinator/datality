import pytest

from datality.van_emde_boas import VEB


def test_van_emde_boas_initialize():
    """create a veb from a list of values"""
    # empty list
    init = []
    veb = VEB(init)
    assert not veb
    # sinlge value
    init = [7]
    veb = VEB(init)
    assert len(veb) == 1
    # double value
    init = [7, 5]
    veb = VEB(init)
    assert len(veb) == 2
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    veb = VEB(init)
    assert len(veb) == 20


def test_van_emde_boas_search():
    """search in the veb the given value"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    veb = VEB(init)
    assert veb.search(3)
    # empty list
    init = []
    veb = VEB(init)
    with pytest.raises(KeyError):
        veb.search(3)
    # list of words


def test_van_emde_boas_delete():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    veb = VEB(init)
    with pytest.raises(KeyError):
        veb.delete(5)
    # value not found
    init = [7]
    veb = VEB(init)
    with pytest.raises(KeyError):
        veb.delete(8)
    # CLRS killer
    init = []
    veb = VEB(init)
    veb.insert(1)
    veb.insert(2)
    assert len(veb) == 2
    with pytest.raises(KeyError):
        veb.delete(3)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    veb = VEB(init)
    veb.delete(15)
    assert len(veb) == 19
    with pytest.raises(KeyError):
        veb.search(15)
    # delete head
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    veb = VEB(init)
    veb.delete(7)
    assert len(veb) == 19
    with pytest.raises(KeyError):
        veb.search(7)


def test_van_emde_boas_successor():
    """get the successor of the given value"""
    # empty list
    init = []
    veb = VEB(init)
    with pytest.raises(KeyError):
        veb.successor(5)
    # value not found
    init = [8]
    veb = VEB(init)
    with pytest.raises(KeyError):
        print(f"\n{veb.successor(8)}")
        veb.successor(8)
    # no successor on the tree
    init = [7]
    veb = VEB(init)
    with pytest.raises(KeyError):
        veb.successor(7)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    veb = VEB(init)
    assert veb.successor(0) == 1
    assert veb.successor(7) == 8
    assert veb.successor(17) == 18

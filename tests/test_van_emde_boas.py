import pytest

from datality.van_emde_boas import VEB


def test_veb_tree_initialize():
    """create a veb_tree from a list of values"""
    # single item
    init = [7]
    veb = VEB(init)
    assert len(veb) == 16
    # repeated
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16, 7]
    veb = VEB(init)
    assert len(veb) == 64
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    veb = VEB(init)
    assert len(veb) == 64
    # big
    init = [
        249,
        883,
        434,
        66,
        170,
        251,
        518,
        287,
        728,
        407,
        729,
        368,
        716,
        60,
        513,
        167,
        204,
        62,
        282,
        612,
        373,
        515,
        566,
        61,
        551,
        175,
        138,
        633,
        893,
        932,
        474,
        431,
        922,
        497,
        975,
        599,
        598,
        389,
        24,
        93,
        213,
        176,
        295,
        314,
        681,
        799,
        308,
        987,
        546,
        736,
        415,
        975,
        965,
        570,
        748,
        401,
        155,
        840,
        785,
        998,
        578,
        852,
        262,
        720,
        204,
        290,
        383,
        362,
        256,
        61,
        226,
        695,
        956,
        96,
        269,
        182,
        950,
        478,
        824,
        523,
        656,
        219,
        929,
        431,
        522,
        498,
        481,
        237,
        4,
        272,
        980,
        644,
        659,
        824,
        816,
        702,
        908,
        257,
        160,
        707,
    ]
    veb = VEB(init)
    assert len(veb) == 2048
    # empty list
    init = []
    veb = VEB(init)
    assert len(veb) == 4
    # alternative init
    veb = VEB(u=16, keys=[1, 3, 5, 11])
    assert len(veb) == 32
    # alternative init
    with pytest.raises(ValueError):
        veb = VEB(u=-5, keys=[1, 3, 5, 11])
    with pytest.raises(ValueError):
        veb = VEB(u=5, keys=[1, 5, 5, -11])


def test_van_emde_boas_max():
    """get max"""
    # empty list
    init = []
    veb = VEB(init)
    with pytest.raises(IndexError):
        veb.max()
    # value not found
    init = [7]
    veb = VEB(init)
    assert veb.max() == 7
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    veb = VEB(init)
    assert veb.max() == 19


def test_van_emde_boas_min():
    """get min"""
    # empty list
    init = []
    veb = VEB(init)
    with pytest.raises(IndexError):
        veb.min()
    # value not found
    init = [7]
    veb = VEB(init)
    assert veb.min() == 7
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    veb = VEB(init)
    assert veb.min() == 0


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


def test_van_emde_boas_delete():
    """deletes a new node with the given `value`"""
    # empty list
    init = []
    veb = VEB(init)
    veb.delete(5)
    with pytest.raises(KeyError):
        veb.search(5)
    # value not found
    init = [7]
    veb = VEB(init)
    veb.delete(8)
    with pytest.raises(KeyError):
        veb.search(8)
    # CLRS killer
    init = []
    veb = VEB(init)
    veb.insert(1)
    veb.insert(2)
    assert len(veb) == 4
    veb.delete(3)
    with pytest.raises(KeyError):
        veb.search(3)
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    veb = VEB(init)
    veb.delete(15)
    assert len(veb) == 64
    with pytest.raises(KeyError):
        veb.search(15)
    # delete head
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    veb = VEB(init)
    veb.delete(7)
    assert len(veb) == 64
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

def test_van_emde_boas_repr():
    """get repr"""
    # empty list
    init = []
    veb = VEB(init)
    res = """main:
-->(None, None)u4
summary:
"""
    assert repr(veb) == res
    # value not found
    init = [7]
    veb = VEB(init)
    res = """main:
-->(7, 7)u16
summary:
"""
    assert repr(veb) == res
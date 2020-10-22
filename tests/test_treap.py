import pytest

from datality.treap import Treap


def test_treap_tree_initialize():
    """create a treap_tree from a list of values"""
    # single item
    init = [7]
    treap = Treap(init)
    assert len(treap) == 1
    # repeated
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16, 7]
    treap = Treap(init)
    assert len(treap) == 20
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    treap = Treap(init)
    assert len(treap) == 20
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
    treap = Treap(init)
    assert len(treap) == 95
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
    for e in range(20):
        treap.delete(e)
    assert len(treap) == 0
    with pytest.raises(KeyError):
        treap.search(15)
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
    treap = Treap(init)
    for _ in range(95):
        treap.delete(treap.root.value)
    assert len(treap) == 0
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

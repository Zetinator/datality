import pytest
from datality.fenwick_tree import FenwickTree


def test_fenwick_tree_initialize():
    """test the dynamic sums, of a fenwick tree"""
    init = [7, 17, 15, 3, 8, 13, 1, 18]
    res = [0, 7, 24, 15, 42, 8, 21, 1, 82]
    bit = FenwickTree(init)
    # test the correct creation
    assert len(bit.tree) == 9
    assert len(bit) == 8
    assert bit.tree == res


def test_fenwick_tree_query():
    """test the dynamic sums, of a fenwick tree"""
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    bit = FenwickTree(init)
    # test the correct creation
    assert bit.sum(0, 3) == sum(init[0:3])
    assert bit.sum(4, 9) == sum(init[4:9])
    assert bit.sum(0, 0) == sum(init[0:0])
    assert bit.sum(0, len(init)) == sum(init[:])
    # out of range
    with pytest.raises(IndexError):
        bit.sum(-5, 0)
    with pytest.raises(IndexError):
        bit.sum(-5, 200)
    with pytest.raises(IndexError):
        bit.sum(0, 69)


def test_fenwick_tree_repr():
    """test the repr"""
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    bit = FenwickTree(init)
    # test the repr
    res = """[0, 7, 24, 15, 42, 8, 21, 1, 82, 19, 19, 12, 36, 10, 19, 4, 155, 11, 13, 6, 35]"""
    assert repr(bit) == res

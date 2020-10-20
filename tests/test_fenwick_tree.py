from datality.fenwick_tree import FenwickTree


def test_fenwick_tree_initialize():
    """test the dynamic sums, of a fenwick tree"""
    init = [7, 17, 15, 3, 8, 13, 1, 18]
    res = [0, 7, 24, 15, 42, 8, 21, 1, 82]
    bit = FenwickTree(init)
    # test the correct creation
    assert len(bit.tree) == 9
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

import pytest

from datality.segment_tree import SegmentTree


def test_segment_tree_initialize():
    """test the dynamic sums, of a fenwick tree"""
    # empty tree
    init = []
    st = SegmentTree(init)
    # test the correct creation
    assert len(st) == 0
    # single element
    init = [7]
    st = SegmentTree(init)
    # test the correct creation
    assert len(st) == 1
    # common tree odd
    init = [7, 17, 15, 3, 8, 13, 1, 18]
    st = SegmentTree(init)
    # test the correct creation
    assert len(st) == 8
    # common tree even
    init = [7, 17, 15, 3, 8, 13, 1, 18, 20]
    st = SegmentTree(init)
    # test the correct creation
    assert len(st) == 9


def test_segment_tree_query_max():
    """test the dynamic sums, of a fenwick tree"""
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    st = SegmentTree(init)
    # single item
    assert st.query_max(0, 1) == max(init[0:1])
    # head query
    assert st.query_max(0, 3) == max(init[0:4])
    # tail query
    assert st.query_max(9, len(init)) == max(init[9:])
    # common query
    assert st.query_max(4, 9) == max(init[4:10])
    # full array
    assert st.query_max(0, len(init)) == max(init[:])
    # non valids
    with pytest.raises(ValueError):
        st.query_max(0, 0)
    with pytest.raises(ValueError):
        st.query_max(-1, 0)
    with pytest.raises(ValueError):
        st.query_max(0, 69)
    with pytest.raises(ValueError):
        st.query_max(6, 5)

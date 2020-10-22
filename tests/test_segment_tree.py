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


def test_segment_tree_query_min():
    """test the dynamic min"""
    # empty
    init = []
    st = SegmentTree(init)
    with pytest.raises(ValueError):
        st.query_min(0, 1)
    # single
    init = [7]
    st = SegmentTree(init)
    # single item
    assert st.query_min(0, 1) == min(init[0:1])
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    st = SegmentTree(init)
    # single item
    assert st.query_min(0, 1) == min(init[0:1])
    # head query
    assert st.query_min(0, 4) == min(init[0:4])
    # tail query
    assert st.query_min(9, len(init)) == min(init[9:])
    # common query
    assert st.query_min(4, 10) == min(init[4:10])
    # full array
    assert st.query_min(0, len(init)) == min(init[:])
    # non valids
    with pytest.raises(ValueError):
        st.query_min(0, 0)
    with pytest.raises(ValueError):
        st.query_min(-1, 0)
    with pytest.raises(ValueError):
        st.query_min(0, 69)
    with pytest.raises(ValueError):
        st.query_min(6, 5)


def test_segment_tree_query_sum():
    """test the dynamic sum"""
    # empty
    init = []
    st = SegmentTree(init)
    with pytest.raises(ValueError):
        st.query_sum(0, 1)
    # single
    init = [7]
    st = SegmentTree(init)
    # single item
    assert st.query_sum(0, 1) == sum(init[0:1])
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    st = SegmentTree(init)
    # single item
    assert st.query_sum(0, 1) == sum(init[0:1])
    # head query
    assert st.query_sum(0, 4) == sum(init[0:4])
    # tail query
    assert st.query_sum(9, len(init)) == sum(init[9:])
    # common query
    assert st.query_sum(4, 10) == sum(init[4:10])
    # full array
    assert st.query_sum(0, len(init)) == sum(init[:])
    # non valids
    with pytest.raises(ValueError):
        st.query_sum(0, 0)
    with pytest.raises(ValueError):
        st.query_sum(-1, 0)
    with pytest.raises(ValueError):
        st.query_sum(0, 69)
    with pytest.raises(ValueError):
        st.query_sum(6, 5)


def test_segment_tree_query_max():
    """test the dynamic max"""
    # empty
    init = []
    st = SegmentTree(init)
    with pytest.raises(ValueError):
        st.query_max(0, 1)
    # single
    init = [7]
    st = SegmentTree(init)
    # single item
    assert st.query_max(0, 1) == max(init[0:1])
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    st = SegmentTree(init)
    # single item
    assert st.query_max(0, 1) == max(init[0:1])
    # head query
    assert st.query_max(0, 4) == max(init[0:4])
    # tail query
    assert st.query_max(9, len(init)) == max(init[9:])
    # common query
    assert st.query_max(4, 10) == max(init[4:10])
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


def test_segment_tree_repr():
    """test the dynamic max"""
    # empty
    init = []
    st = SegmentTree(init)
    res = """"""
    assert repr(st) == res
    # single
    init = [7]
    st = SegmentTree(init)
    res = """-->(7, 7, 7)[0, 0]"""
    assert repr(st) == res
    # common
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    st = SegmentTree(init)
    res = """				-->(16, 16, 16)[19, 19]
			-->(16, 6, 22)[18, 19]
				-->(6, 6, 6)[18, 18]
		-->(16, 2, 49)[15, 19]
				-->(2, 2, 2)[17, 17]
			-->(14, 2, 27)[15, 17]
					-->(11, 11, 11)[16, 16]
				-->(14, 11, 25)[15, 16]
					-->(14, 14, 14)[15, 15]
	-->(16, 2, 89)[10, 19]
				-->(4, 4, 4)[14, 14]
			-->(9, 4, 13)[13, 14]
				-->(9, 9, 9)[13, 13]
		-->(12, 4, 40)[10, 14]
				-->(10, 10, 10)[12, 12]
			-->(12, 5, 27)[10, 12]
					-->(5, 5, 5)[11, 11]
				-->(12, 5, 17)[10, 11]
					-->(12, 12, 12)[10, 10]
-->(19, 0, 190)[0, 19]
				-->(0, 0, 0)[9, 9]
			-->(19, 0, 19)[8, 9]
				-->(19, 19, 19)[8, 8]
		-->(19, 0, 51)[5, 9]
				-->(18, 18, 18)[7, 7]
			-->(18, 1, 32)[5, 7]
					-->(1, 1, 1)[6, 6]
				-->(13, 1, 14)[5, 6]
					-->(13, 13, 13)[5, 5]
	-->(19, 0, 101)[0, 9]
				-->(8, 8, 8)[4, 4]
			-->(8, 3, 11)[3, 4]
				-->(3, 3, 3)[3, 3]
		-->(17, 3, 50)[0, 4]
				-->(15, 15, 15)[2, 2]
			-->(17, 7, 39)[0, 2]
					-->(17, 17, 17)[1, 1]
				-->(17, 7, 24)[0, 1]
					-->(7, 7, 7)[0, 0]"""
    assert repr(st) == res

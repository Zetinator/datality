from datality.disjoint_set import DJS


def test_bst_union_find():
    """test disjoint sets with my friends"""
    djs = DJS()
    djs.union("erick", "sophia")
    djs.union("kim", "sophia")
    djs.union("aldo", "valeria")
    assert not djs.same("aldo", "erick")
    assert djs.same("kim", "erick")
    djs.union("aldo", "kim")
    assert djs.same("valeria", "erick")

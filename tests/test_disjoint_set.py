from datality.disjoint_set import DJS


def test_djs_make_set():
    """test disjoint sets with my friends"""
    djs = DJS()
    djs.make_set("erick")
    djs.make_set("sophia")
    djs.make_set("kim")
    # sad but true...
    assert not djs.same("erick", "kim")
    assert len(djs) == 3


def test_djs_union_find():
    """test disjoint sets with my friends"""
    djs = DJS()
    # initialize sets
    djs.make_set("erick")
    djs.make_set("sophia")
    djs.make_set("kim")
    djs.make_set("aldo")
    djs.make_set("valeria")
    # make some friendships
    djs.union("erick", "sophia")
    djs.union("kim", "sophia")
    djs.union("aldo", "valeria")
    assert len(djs) == 2
    # union not friends
    assert not djs.same("aldo", "erick")
    # friends
    assert djs.same("kim", "erick")
    djs.union("aldo", "kim")
    assert len(djs) == 1
    assert djs.same("valeria", "erick")
    # union on same set
    djs.union("erick", "kim")
    assert len(djs) == 1


def test_djs_repr():
    """test disjoint sets with my friends"""
    djs = DJS()
    # initialize sets
    djs.make_set("erick")
    djs.make_set("sophia")
    djs.make_set("kim")
    djs.make_set("aldo")
    djs.make_set("valeria")
    # make some friendships
    djs.union("erick", "sophia")
    djs.union("kim", "sophia")
    djs.union("aldo", "valeria")
    # repr
    res = """{'erick': 'sophia', 'sophia': 'sophia', 'kim': 'sophia', 'aldo': 'valeria', 'valeria': 'valeria'}"""
    assert repr(djs) == res

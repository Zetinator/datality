import pytest
from datality.radix_trie import RadixTree


def test_radix_tree_initialize():
    """create a rt from a list of values"""
    # empty list
    init = []
    rt = RadixTree(init)
    assert not rt
    # single item
    init = ['sophia']
    rt = RadixTree(init)
    assert len(rt) == len(init)
    # common list of values
    init = ['sophia', 'marion', 'erick', 'erika', 'mariana', 'marianalia']
    rt = RadixTree(init)
    assert len(rt) == len(init)


def test_radix_tree_search():
    """create a rt from a list of values"""
    # empty list
    init = []
    rt = RadixTree(init)
    with pytest.raises(KeyError):
        rt.search('marion')
    # single item
    init = ['sophia']
    rt = RadixTree(init)
    assert rt.search('sophia').value == 'sophia'
    with pytest.raises(KeyError):
        rt.search('marion')
    # common list of values
    init = ['sophia', 'marion', 'erick', 'erika', 'mariana', 'marianalia']
    rt = RadixTree(init)
    assert rt.search('erika').value == 'erika'
    with pytest.raises(KeyError):
        rt.search('kim')


def test_radix_tree_predict():
    """create a rt from a list of values"""
    # empty list
    init = []
    rt = RadixTree(init)
    assert rt.predict('marion') == []
    # single item
    init = ['sophia']
    rt = RadixTree(init)
    assert rt.predict('sop') == init
    assert rt.predict('') == init
    # common list of values
    init = ['sophia', 'marion', 'erick', 'erika', 'mariana', 'marianalia']
    rt = RadixTree(init)
    assert set(rt.predict('eri')) == set(['erick', 'erika'])
    assert set(rt.predict('mari')) == set(['mariana', 'marion', 'marianalia'])

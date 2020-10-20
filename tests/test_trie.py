import pytest
from collectionz.trie import Trie


def test_trie_initialize():
    """create a trie from a list of values"""
    # empty list
    init = []
    trie = Trie(init)
    assert not trie
    # single item
    init = ['sophia']
    trie = Trie(init)
    assert len(trie) == len(init)
    # common list of values
    init = ['sophia', 'marion', 'erick', 'erika', 'mariana']
    trie = Trie(init)
    assert len(trie) == len(init)


def test_trie_search():
    """create a trie from a list of values"""
    # empty list
    init = []
    trie = Trie(init)
    with pytest.raises(KeyError):
        trie.search('marion')
    # single item
    init = ['sophia']
    trie = Trie(init)
    assert trie.search('sophia').value == 'sophia'
    with pytest.raises(KeyError):
        trie.search('marion')
    # common list of values
    init = ['sophia', 'marion', 'erick', 'erika', 'mariana']
    trie = Trie(init)
    assert trie.search('erika').value == 'erika'
    with pytest.raises(KeyError):
        trie.search('kim')


def test_trie_delete():
    """create a trie from a list of values"""
    # empty list
    init = []
    trie = Trie(init)
    with pytest.raises(KeyError):
        trie.delete('marion')
    # single item
    init = ['sophia']
    trie = Trie(init)
    trie.delete('sophia')
    with pytest.raises(KeyError):
        trie.search('sophia')
    # common list of values
    init = ['sophia', 'marion', 'erick', 'erika', 'mariana']
    trie = Trie(init)
    trie.delete('erika')
    assert trie.search('erick').value == 'erick'
    with pytest.raises(KeyError):
        trie.search('erika')


def test_trie_predict():
    """create a trie from a list of values"""
    # empty list
    init = []
    trie = Trie(init)
    assert trie.predict('marion') == []
    # single item
    init = ['sophia']
    trie = Trie(init)
    assert trie.predict('sop') == init
    assert trie.predict('') == init
    # common list of values
    init = ['sophia', 'marion', 'erick', 'erika', 'mariana']
    trie = Trie(init)
    assert set(trie.predict('eri')) == set(['erick', 'erika'])
    assert set(trie.predict('mari')) == set(['mariana', 'marion'])
    assert set(trie.predict('mariano')) == set()

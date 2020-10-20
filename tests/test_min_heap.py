import pytest
from datality.min_heap import Heap


def test_heap_initialize():
    """create a heap a list of values"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    heap = Heap(init)
    assert len(heap) == 20
    # empty list
    init = []
    heap = Heap(init)
    assert not heap
    # list of words
    init = ["erick", "sophia", "marion"]
    heap = Heap(init)
    assert len(heap) == 3
    # list of tuples
    init = [(1, 4), (5, 5), (1, 3), (2, 10)]
    heap = Heap(init)
    assert len(heap) == 4


def test_heap_push():
    """search in the heap the given value"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    heap = Heap(init)
    heap.push(-1)
    assert heap.peek() == -1
    # empty list
    init = []
    heap = Heap(init)
    heap.push(-1)
    assert heap.peek() == -1
    # list of words
    init = ["erick", "sophia", "marion"]
    heap = Heap(init)
    heap.push("aldo")
    assert heap.peek() == "aldo"
    # list of tuples
    init = [(1, 4), (5, 5), (1, 3), (2, 10)]
    heap = Heap(init)
    heap.push((1, 1))
    assert heap.peek() == (1, 1)


def test_heap_peek():
    """deletes a new node with the given `value`"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    heap = Heap(init)
    assert heap.peek() == 0
    # empty list
    init = []
    heap = Heap(init)
    with pytest.raises(IndexError):
        heap.peek()


def test_heap_pop():
    """deletes a new node with the given `value`"""
    # common list of values
    init = [7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16]
    heap = Heap(init)
    for i in range(len(heap)):
        assert heap.pop() == i
    # empty list
    init = []
    heap = Heap(init)
    with pytest.raises(IndexError):
        heap.pop()

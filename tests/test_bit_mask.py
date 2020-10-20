from datality.bit_mask import BitMask


def test_bit_mask_set():
    """sets a bit in a number"""
    # common
    init = 5
    res = BitMask.set(init, 1)
    assert res == 7
    # set 0
    init = 0
    res = BitMask.set(init, 0)
    assert res == 1
    # set at out of range
    init = 5
    res = BitMask.set(init, 3)
    assert res == 13


def test_bit_mask_toggle():
    """toggles a bit in a number"""
    # common
    init = 5
    res = BitMask.toggle(init, 0)
    assert res == 4
    # set
    init = 0
    res = BitMask.toggle(init, 0)
    assert res == 1
    # set at out of range
    init = 5
    res = BitMask.toggle(init, 3)
    assert res == 13


def test_bit_mask_check():
    """checks a bit in a number"""
    # common
    init = 5
    res = BitMask.check(init, 0)
    assert res
    res = BitMask.check(init, 1)
    assert not res
    res = BitMask.check(init, 2)
    assert res


def test_bit_mask_clear():
    """clears a bit in a number"""
    # common
    init = 5
    res = BitMask.clear(init)
    assert res == 0


def test_bit_mask_reset():
    """resets a bit in a number"""
    # common
    init = 5
    res = BitMask.reset(init, 0)
    assert res == 4
    # set 0
    init = 0
    res = BitMask.reset(init, 0)
    assert res == 0
    # set at out of range
    init = 5
    res = BitMask.reset(init, 3)
    assert res == 5

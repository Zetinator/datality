import pytest

from datality.trie import Trie


def test_trie_initialize():
    """create a trie from a list of values"""
    # empty list
    init = []
    trie = Trie(init)
    assert not trie
    # single item
    init = ["sophia"]
    trie = Trie(init)
    assert len(trie) == len(init)
    # repeated
    init = ["sophia", "marion", "erick", "erika", "mariana", "sophia"]
    trie = Trie(init)
    assert len(trie) == len(init) - 1
    # common list of values
    init = ["sophia", "marion", "erick", "erika", "mariana"]
    trie = Trie(init)
    assert len(trie) == len(init)
    # big one (is repeated)
    init = [
        "WJRW",
        "0XNxMl3i",
        "J5JJqZL0pREJcg",
        "3xBb_EFo-cP9vgnACA",
        "5K8",
        "8A",
        "K14LTBNpOpfgLg1EzbwVnw",
        "Jw",
        "USWAEqcBLnXU22EgqQ",
        "sSHzNcSTv4JpWT8",
        "-LdAkDeJwLiQ",
        "pSeoWYSGIFZS",
        "qWdomzPReP84OO__DPst9N6f3A",
        "bhxo_ztcxpzgg1CrGQ",
        "U-N0qdjGX0RuEqs",
        "bPtyMvG7xCTqzRQQWJsxMQ",
        "4LVIgN2F1f5qgj7-lTqk",
        "7HdZIlgt5ESwsU-Q23Qw0mM",
        "1YPv",
        "nhTQ4AnmeJ8",
        "0dgP9Ys",
        "ELABBB-yBy-J5Fy9wAK4RKKPOA",
        "m6v1W5EEYS0xK-SaNLfT",
        "mr3BwT0nrMsS5-VfIZiv1HA",
        "laQ8k0UdMN8b-DMp3wtdVTvv",
        "f1LTAtpPbPQ",
        "cPFF3fiQl-q-SA",
        "jzGTlF8O5xGI21o",
        "kQyuJ9AS",
        "z_B5",
        "w69mwZMwoqAAzA",
        "5PCN9LxDd0SKZUR-n4IR",
        "uyVnrGcgCXj1tw",
        "",
        "opbT4Z6N9Q",
        "Nt8bqTuDVMUyNsxkrPoLAmbUPg",
        "RVCSc2aVKZ28WsVFtgfMrSa4uA",
        "KES6",
        "jdQ",
        "8Q",
        "GA",
        "XWPB3tORIms",
        "",
        "VqkMDaMFdOWtGg",
        "tP68Qun3Ueu40YklB8ky6kk",
        "8S0",
        "2Yty6PUc",
        "N6w",
        "-Cv1l66cqlU6M0Q",
        "sTAB9olwitV8jSYVJg4",
    ]
    trie = Trie(init)
    assert len(trie) == 49


def test_trie_search():
    """create a trie from a list of values"""
    # empty list
    init = []
    trie = Trie(init)
    with pytest.raises(KeyError):
        trie.search("marion")
    # single item
    init = ["sophia"]
    trie = Trie(init)
    assert trie.search("sophia").value == "sophia"
    with pytest.raises(KeyError):
        trie.search("marion")
    # common list of values
    init = ["sophia", "marion", "erick", "erika", "mariana"]
    trie = Trie(init)
    assert trie.search("erika").value == "erika"
    with pytest.raises(KeyError):
        trie.search("kim")
    # big
    init = [
        "WJRW",
        "0XNxMl3i",
        "J5JJqZL0pREJcg",
        "3xBb_EFo-cP9vgnACA",
        "5K8",
        "8A",
        "K14LTBNpOpfgLg1EzbwVnw",
        "Jw",
        "USWAEqcBLnXU22EgqQ",
        "sSHzNcSTv4JpWT8",
        "-LdAkDeJwLiQ",
        "pSeoWYSGIFZS",
        "qWdomzPReP84OO__DPst9N6f3A",
        "bhxo_ztcxpzgg1CrGQ",
        "U-N0qdjGX0RuEqs",
        "bPtyMvG7xCTqzRQQWJsxMQ",
        "4LVIgN2F1f5qgj7-lTqk",
        "7HdZIlgt5ESwsU-Q23Qw0mM",
        "1YPv",
        "nhTQ4AnmeJ8",
        "0dgP9Ys",
        "ELABBB-yBy-J5Fy9wAK4RKKPOA",
        "m6v1W5EEYS0xK-SaNLfT",
        "mr3BwT0nrMsS5-VfIZiv1HA",
        "laQ8k0UdMN8b-DMp3wtdVTvv",
        "f1LTAtpPbPQ",
        "cPFF3fiQl-q-SA",
        "jzGTlF8O5xGI21o",
        "kQyuJ9AS",
        "z_B5",
        "w69mwZMwoqAAzA",
        "5PCN9LxDd0SKZUR-n4IR",
        "uyVnrGcgCXj1tw",
        "",
        "opbT4Z6N9Q",
        "Nt8bqTuDVMUyNsxkrPoLAmbUPg",
        "RVCSc2aVKZ28WsVFtgfMrSa4uA",
        "KES6",
        "jdQ",
        "8Q",
        "GA",
        "XWPB3tORIms",
        "",
        "VqkMDaMFdOWtGg",
        "tP68Qun3Ueu40YklB8ky6kk",
        "8S0",
        "2Yty6PUc",
        "N6w",
        "-Cv1l66cqlU6M0Q",
        "sTAB9olwitV8jSYVJg4",
    ]
    trie = Trie(init)
    trie.search("USWAEqcBLnXU22EgqQ").value == "USWAEqcBLnXU22EgqQ"


def test_trie_delete():
    """create a trie from a list of values"""
    # empty list
    init = []
    trie = Trie(init)
    with pytest.raises(KeyError):
        trie.delete("marion")
    # single item
    init = ["sophia"]
    trie = Trie(init)
    trie.delete("sophia")
    with pytest.raises(KeyError):
        trie.search("sophia")
    # common list of values
    init = ["sophia", "marion", "erick", "erika", "mariana"]
    trie = Trie(init)
    trie.delete("erika")
    assert trie.search("erick").value == "erick"
    with pytest.raises(KeyError):
        trie.search("erika")
    # big
    init = [
        "WJRW",
        "0XNxMl3i",
        "J5JJqZL0pREJcg",
        "3xBb_EFo-cP9vgnACA",
        "5K8",
        "8A",
        "K14LTBNpOpfgLg1EzbwVnw",
        "Jw",
        "USWAEqcBLnXU22EgqQ",
        "sSHzNcSTv4JpWT8",
        "-LdAkDeJwLiQ",
        "pSeoWYSGIFZS",
        "qWdomzPReP84OO__DPst9N6f3A",
        "bhxo_ztcxpzgg1CrGQ",
        "U-N0qdjGX0RuEqs",
        "bPtyMvG7xCTqzRQQWJsxMQ",
        "4LVIgN2F1f5qgj7-lTqk",
        "7HdZIlgt5ESwsU-Q23Qw0mM",
        "1YPv",
        "nhTQ4AnmeJ8",
        "0dgP9Ys",
        "ELABBB-yBy-J5Fy9wAK4RKKPOA",
        "m6v1W5EEYS0xK-SaNLfT",
        "mr3BwT0nrMsS5-VfIZiv1HA",
        "laQ8k0UdMN8b-DMp3wtdVTvv",
        "f1LTAtpPbPQ",
        "cPFF3fiQl-q-SA",
        "jzGTlF8O5xGI21o",
        "kQyuJ9AS",
        "z_B5",
        "w69mwZMwoqAAzA",
        "5PCN9LxDd0SKZUR-n4IR",
        "uyVnrGcgCXj1tw",
        "",
        "opbT4Z6N9Q",
        "Nt8bqTuDVMUyNsxkrPoLAmbUPg",
        "RVCSc2aVKZ28WsVFtgfMrSa4uA",
        "KES6",
        "jdQ",
        "8Q",
        "GA",
        "XWPB3tORIms",
        "",
        "VqkMDaMFdOWtGg",
        "tP68Qun3Ueu40YklB8ky6kk",
        "8S0",
        "2Yty6PUc",
        "N6w",
        "-Cv1l66cqlU6M0Q",
        "sTAB9olwitV8jSYVJg4",
    ]
    trie = Trie(init)
    for e in set(init):
        trie.delete(e)
    assert len(trie) == 0


def test_trie_predict():
    """create a trie from a list of values"""
    # empty list
    init = []
    trie = Trie(init)
    assert trie.predict("marion") == []
    # single item
    init = ["sophia"]
    trie = Trie(init)
    assert trie.predict("sop") == init
    assert trie.predict("") == init
    # common list of values
    init = ["sophia", "marion", "erick", "erika", "mariana"]
    trie = Trie(init)
    assert set(trie.predict("eri")) == set(["erick", "erika"])
    assert set(trie.predict("mari")) == set(["mariana", "marion"])
    assert set(trie.predict("mariano")) == set()


def test_trie_repr():
    """test repr"""
    # empty list
    init = []
    trie = Trie(init)
    res = """"""
    assert repr(trie) == res
    # single item
    init = ["sophia"]
    trie = Trie(init)
    res = """-(s)-(o)-(p)-(h)-(i)-(a)
                        sophia
"""
    assert repr(trie) == res
    # common list of values
    init = ["sophia", "marion", "erick", "erika", "mariana"]
    trie = Trie(init)
    res = """-(s)-(o)-(p)-(h)-(i)-(a)
                        sophia
-(m)-(a)-(r)-(i)-(o)-(n)
                        marion
                -(a)-(n)-(a)
                            mariana
-(e)-(r)-(i)-(c)-(k)
                    erick
            -(k)-(a)
                    erika
"""
    assert repr(trie) == res
    # big
    init = [
        "WJRW",
        "0XNxMl3i",
        "J5JJqZL0pREJcg",
        "3xBb_EFo-cP9vgnACA",
        "5K8",
        "8A",
        "K14LTBNpOpfgLg1EzbwVnw",
        "Jw",
        "USWAEqcBLnXU22EgqQ",
        "sSHzNcSTv4JpWT8",
        "-LdAkDeJwLiQ",
        "pSeoWYSGIFZS",
        "qWdomzPReP84OO__DPst9N6f3A",
        "bhxo_ztcxpzgg1CrGQ",
        "U-N0qdjGX0RuEqs",
        "bPtyMvG7xCTqzRQQWJsxMQ",
        "4LVIgN2F1f5qgj7-lTqk",
        "7HdZIlgt5ESwsU-Q23Qw0mM",
        "1YPv",
        "nhTQ4AnmeJ8",
        "0dgP9Ys",
        "ELABBB-yBy-J5Fy9wAK4RKKPOA",
        "m6v1W5EEYS0xK-SaNLfT",
        "mr3BwT0nrMsS5-VfIZiv1HA",
        "laQ8k0UdMN8b-DMp3wtdVTvv",
        "f1LTAtpPbPQ",
        "cPFF3fiQl-q-SA",
        "jzGTlF8O5xGI21o",
        "kQyuJ9AS",
        "z_B5",
        "w69mwZMwoqAAzA",
        "5PCN9LxDd0SKZUR-n4IR",
        "uyVnrGcgCXj1tw",
        "",
        "opbT4Z6N9Q",
        "Nt8bqTuDVMUyNsxkrPoLAmbUPg",
        "RVCSc2aVKZ28WsVFtgfMrSa4uA",
        "KES6",
        "jdQ",
        "8Q",
        "GA",
        "XWPB3tORIms",
        "",
        "VqkMDaMFdOWtGg",
        "tP68Qun3Ueu40YklB8ky6kk",
        "8S0",
        "2Yty6PUc",
        "N6w",
        "-Cv1l66cqlU6M0Q",
        "sTAB9olwitV8jSYVJg4",
    ]
    trie = Trie(init)
    res = """

-(W)-(J)-(R)-(W)
                WJRW
-(0)-(X)-(N)-(x)-(M)-(l)-(3)-(i)
                                0XNxMl3i
    -(d)-(g)-(P)-(9)-(Y)-(s)
                            0dgP9Ys
-(J)-(5)-(J)-(J)-(q)-(Z)-(L)-(0)-(p)-(R)-(E)-(J)-(c)-(g)
                                                        J5JJqZL0pREJcg
    -(w)
        Jw
-(3)-(x)-(B)-(b)-(_)-(E)-(F)-(o)-(-)-(c)-(P)-(9)-(v)-(g)-(n)-(A)-(C)-(A)
                                                                        3xBb_EFo-cP9vgnACA
-(5)-(K)-(8)
            5K8
    -(P)-(C)-(N)-(9)-(L)-(x)-(D)-(d)-(0)-(S)-(K)-(Z)-(U)-(R)-(-)-(n)-(4)-(I)-(R)
                                                                                5PCN9LxDd0SKZUR-n4IR
-(8)-(A)
        8A
    -(Q)
        8Q
    -(S)-(0)
            8S0
-(K)-(1)-(4)-(L)-(T)-(B)-(N)-(p)-(O)-(p)-(f)-(g)-(L)-(g)-(1)-(E)-(z)-(b)-(w)-(V)-(n)-(w)
                                                                                        K14LTBNpOpfgLg1EzbwVnw
    -(E)-(S)-(6)
                KES6
-(U)-(S)-(W)-(A)-(E)-(q)-(c)-(B)-(L)-(n)-(X)-(U)-(2)-(2)-(E)-(g)-(q)-(Q)
                                                                        USWAEqcBLnXU22EgqQ
    -(-)-(N)-(0)-(q)-(d)-(j)-(G)-(X)-(0)-(R)-(u)-(E)-(q)-(s)
                                                            U-N0qdjGX0RuEqs
-(s)-(S)-(H)-(z)-(N)-(c)-(S)-(T)-(v)-(4)-(J)-(p)-(W)-(T)-(8)
                                                            sSHzNcSTv4JpWT8
    -(T)-(A)-(B)-(9)-(o)-(l)-(w)-(i)-(t)-(V)-(8)-(j)-(S)-(Y)-(V)-(J)-(g)-(4)
                                                                            sTAB9olwitV8jSYVJg4
-(-)-(L)-(d)-(A)-(k)-(D)-(e)-(J)-(w)-(L)-(i)-(Q)
                                                -LdAkDeJwLiQ
    -(C)-(v)-(1)-(l)-(6)-(6)-(c)-(q)-(l)-(U)-(6)-(M)-(0)-(Q)
                                                            -Cv1l66cqlU6M0Q
-(p)-(S)-(e)-(o)-(W)-(Y)-(S)-(G)-(I)-(F)-(Z)-(S)
                                                pSeoWYSGIFZS
-(q)-(W)-(d)-(o)-(m)-(z)-(P)-(R)-(e)-(P)-(8)-(4)-(O)-(O)-(_)-(_)-(D)-(P)-(s)-(t)-(9)-(N)-(6)-(f)-(3)-(A)
                                                                                                        qWdomzPReP84OO__DPst9N6f3A
-(b)-(h)-(x)-(o)-(_)-(z)-(t)-(c)-(x)-(p)-(z)-(g)-(g)-(1)-(C)-(r)-(G)-(Q)
                                                                        bhxo_ztcxpzgg1CrGQ
    -(P)-(t)-(y)-(M)-(v)-(G)-(7)-(x)-(C)-(T)-(q)-(z)-(R)-(Q)-(Q)-(W)-(J)-(s)-(x)-(M)-(Q)
                                                                                        bPtyMvG7xCTqzRQQWJsxMQ
-(4)-(L)-(V)-(I)-(g)-(N)-(2)-(F)-(1)-(f)-(5)-(q)-(g)-(j)-(7)-(-)-(l)-(T)-(q)-(k)
                                                                                4LVIgN2F1f5qgj7-lTqk
-(7)-(H)-(d)-(Z)-(I)-(l)-(g)-(t)-(5)-(E)-(S)-(w)-(s)-(U)-(-)-(Q)-(2)-(3)-(Q)-(w)-(0)-(m)-(M)
                                                                                            7HdZIlgt5ESwsU-Q23Qw0mM
-(1)-(Y)-(P)-(v)
                1YPv
-(n)-(h)-(T)-(Q)-(4)-(A)-(n)-(m)-(e)-(J)-(8)
                                            nhTQ4AnmeJ8
-(E)-(L)-(A)-(B)-(B)-(B)-(-)-(y)-(B)-(y)-(-)-(J)-(5)-(F)-(y)-(9)-(w)-(A)-(K)-(4)-(R)-(K)-(K)-(P)-(O)-(A)
                                                                                                        ELABBB-yBy-J5Fy9wAK4RKKPOA
-(m)-(6)-(v)-(1)-(W)-(5)-(E)-(E)-(Y)-(S)-(0)-(x)-(K)-(-)-(S)-(a)-(N)-(L)-(f)-(T)
                                                                                m6v1W5EEYS0xK-SaNLfT
    -(r)-(3)-(B)-(w)-(T)-(0)-(n)-(r)-(M)-(s)-(S)-(5)-(-)-(V)-(f)-(I)-(Z)-(i)-(v)-(1)-(H)-(A)
                                                                                            mr3BwT0nrMsS5-VfIZiv1HA
-(l)-(a)-(Q)-(8)-(k)-(0)-(U)-(d)-(M)-(N)-(8)-(b)-(-)-(D)-(M)-(p)-(3)-(w)-(t)-(d)-(V)-(T)-(v)-(v)
                                                                                                laQ8k0UdMN8b-DMp3wtdVTvv
-(f)-(1)-(L)-(T)-(A)-(t)-(p)-(P)-(b)-(P)-(Q)
                                            f1LTAtpPbPQ
-(c)-(P)-(F)-(F)-(3)-(f)-(i)-(Q)-(l)-(-)-(q)-(-)-(S)-(A)
                                                        cPFF3fiQl-q-SA
-(j)-(z)-(G)-(T)-(l)-(F)-(8)-(O)-(5)-(x)-(G)-(I)-(2)-(1)-(o)
                                                            jzGTlF8O5xGI21o
    -(d)-(Q)
            jdQ
-(k)-(Q)-(y)-(u)-(J)-(9)-(A)-(S)
                                kQyuJ9AS
-(z)-(_)-(B)-(5)
                z_B5
-(w)-(6)-(9)-(m)-(w)-(Z)-(M)-(w)-(o)-(q)-(A)-(A)-(z)-(A)
                                                        w69mwZMwoqAAzA
-(u)-(y)-(V)-(n)-(r)-(G)-(c)-(g)-(C)-(X)-(j)-(1)-(t)-(w)
                                                        uyVnrGcgCXj1tw
-(o)-(p)-(b)-(T)-(4)-(Z)-(6)-(N)-(9)-(Q)
                                        opbT4Z6N9Q
-(N)-(t)-(8)-(b)-(q)-(T)-(u)-(D)-(V)-(M)-(U)-(y)-(N)-(s)-(x)-(k)-(r)-(P)-(o)-(L)-(A)-(m)-(b)-(U)-(P)-(g)
                                                                                                        Nt8bqTuDVMUyNsxkrPoLAmbUPg
    -(6)-(w)
            N6w
-(R)-(V)-(C)-(S)-(c)-(2)-(a)-(V)-(K)-(Z)-(2)-(8)-(W)-(s)-(V)-(F)-(t)-(g)-(f)-(M)-(r)-(S)-(a)-(4)-(u)-(A)
                                                                                                        RVCSc2aVKZ28WsVFtgfMrSa4uA
-(G)-(A)
        GA
-(X)-(W)-(P)-(B)-(3)-(t)-(O)-(R)-(I)-(m)-(s)
                                            XWPB3tORIms
-(V)-(q)-(k)-(M)-(D)-(a)-(M)-(F)-(d)-(O)-(W)-(t)-(G)-(g)
                                                        VqkMDaMFdOWtGg
-(t)-(P)-(6)-(8)-(Q)-(u)-(n)-(3)-(U)-(e)-(u)-(4)-(0)-(Y)-(k)-(l)-(B)-(8)-(k)-(y)-(6)-(k)-(k)
                                                                                            tP68Qun3Ueu40YklB8ky6kk
-(2)-(Y)-(t)-(y)-(6)-(P)-(U)-(c)
                                2Yty6PUc
"""
    assert repr(trie) == res

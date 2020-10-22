import pytest

from datality.radix_trie import RadixTree


def test_radix_tree_initialize():
    """create a rt from a list of values"""
    # empty list
    init = []
    rt = RadixTree(init)
    assert not rt
    # single item
    init = ["sophia"]
    rt = RadixTree(init)
    assert len(rt) == len(init)
    # common list of values
    init = ["sophia", "marion", "erick", "erika", "mariana", "marianalia"]
    rt = RadixTree(init)
    assert len(rt) == len(init)
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
    rt = RadixTree(init)
    assert len(rt) == len(init)


def test_radix_tree_search():
    """create a rt from a list of values"""
    # empty list
    init = []
    rt = RadixTree(init)
    with pytest.raises(KeyError):
        rt.search("marion")
    # single item
    init = ["sophia"]
    rt = RadixTree(init)
    assert rt.search("sophia").value == "sophia"
    with pytest.raises(KeyError):
        rt.search("marion")
    # common list of values
    init = ["sophia", "marion", "erick", "erika", "mariana", "marianalia"]
    rt = RadixTree(init)
    assert rt.search("erika").value == "erika"
    with pytest.raises(KeyError):
        rt.search("kim")
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
    rt = RadixTree(init)
    assert rt.search("USWAEqcBLnXU22EgqQ").value == "USWAEqcBLnXU22EgqQ"


def test_radix_tree_predict():
    """create a rt from a list of values"""
    # empty list
    init = []
    rt = RadixTree(init)
    assert rt.predict("marion") == []
    # single item
    init = ["sophia"]
    rt = RadixTree(init)
    assert rt.predict("sop") == init
    assert rt.predict("") == init
    # common list of values
    init = ["sophia", "marion", "erick", "erika", "mariana", "marianalia"]
    rt = RadixTree(init)
    assert set(rt.predict("eri")) == set(["erick", "erika"])
    assert set(rt.predict("mari")) == set(["mariana", "marion", "marianalia"])


def test_radix_tree_repr():
    """test repr"""
    # empty list
    init = []
    rt = RadixTree(init)
    res = """"""
    assert repr(rt) == res
    # single item
    init = ["sophia"]
    rt = RadixTree(init)
    res = """--<sophia>--
(sophia)
"""
    assert repr(rt) == res
    # common list of values
    init = ["sophia", "marion", "erick", "erika", "mariana", "marianalia"]
    rt = RadixTree(init)
    res = """--<sophia>--
(sophia)
--<eri>--
	--<ck>--
	(erick)
	--<ka>--
	(erika)
--<mari>--
	--<on>--
	(marion)
	--<ana>--
	(mariana)
		--<lia>--
		(marianalia)
"""
    assert repr(rt) == res
    init = ["romane", "romanus", "romulus", "rubens", "ruber", "rubicon", "rubicundus"]
    rt = RadixTree(init)
    res = """--<r>--
	--<om>--
		--<an>--
			--<e>--
			(romane)
			--<us>--
			(romanus)
		--<ulus>--
		(romulus)
	--<ub>--
		--<e>--
			--<ns>--
			(rubens)
			--<r>--
			(ruber)
		--<ic>--
			--<on>--
			(rubicon)
			--<undus>--
			(rubicundus)
"""
    assert repr(rt) == res

datality
===========

..  image:: https://github.com/Zetinator/datality/workflows/test/badge.svg?branch=main
    :target: https://github.com/Zetinator/datality/workflows/test/


..  image:: https://github.com/Zetinator/datality/workflows/Upload%20Python%20Package/badge.svg?branch=main
    :target: https://github.com/Zetinator/datality/workflows/Upload%20Python%20Package/



..  image:: https://codecov.io/gh/Zetinator/datality/branch/main/graph/badge.svg?token=AFJ36BHDQ7
    :target: https://codecov.io/gh/Zetinator/datality
    


this package contains implementations from the classic data structures in the *CLRS*

Currently supported data structures:

* `AVL (Adelson-Velsky and Landis) <https://en.wikipedia.org/wiki/AVL_tree>`_

* `BitMask <https://en.wikipedia.org/wiki/Mask_(computing)#:~:text=In%20computer%20science%2C%20a%20mask,in%20a%20single%20bitwise%20operation.>`_

* `BST (binary search tree) <https://en.wikipedia.org/wiki/Binary_search_tree>`_

* `Deque <https://en.wikipedia.org/wiki/Double-ended_queue>`_

* `DJS (disjoint sets) <https://en.wikipedia.org/wiki/Disjoint-set_data_structure>`_

* `DoubleLinkedList <https://en.wikipedia.org/wiki/Doubly_linked_list>`_

* `FenwickTree (bonary indexed tree) <https://en.wikipedia.org/wiki/Fenwick_tree>`_

* `LinkedList <https://en.wikipedia.org/wiki/Linked_list>`_

* `Heap (min heap) <https://en.wikipedia.org/wiki/Heap_(data_structure)>`_

* `RadixTree <https://en.wikipedia.org/wiki/Radix_tree>`_

* `RBTree (red–black tree) <https://en.wikipedia.org/wiki/Red%E2%80%93black_tree>`_

* `SegmentTree <https://en.wikipedia.org/wiki/Segment_tree>`_

* `SkipList <https://en.wikipedia.org/wiki/Skip_list>`_

* `SplayTree <https://en.wikipedia.org/wiki/Splay_tree>`_

* `Treap (bst + heap) <https://en.wikipedia.org/wiki/Treap>`_

* `Trie <https://en.wikipedia.org/wiki/Trie>`_

* `VEB (van Emde Boas tree) <https://en.wikipedia.org/wiki/Van_Emde_Boas_tree>`_


All the implementations have an intuitive `__repr__()` function i.e.

..  code-block:: python

    from datality import AVL
    avl = AVL([7, 17, 15, 3, 8, 13, 1, 18, 19, 0, 12, 5, 10, 9, 4, 14, 11, 2, 6, 16])
    print(avl)
                -->(19)
            -->(18)
                -->(17)
                    -->(16)
        -->(15)
                    -->(14)
                -->(13)
            -->(12)
                    -->(11)
                -->(10)
                    -->(9)
    -->(8)
                -->(7)
                    -->(6)
            -->(5)
                -->(4)
        -->(3)
                -->(2)
            -->(1)
                -->(0)


installation
~~~~~~~~~~~~

..  code-block:: bash

    pip3 install datality


usage
~~~~~
import as any other module with the following statement:

..  code-block:: python

    
    # from datality.avl import AVL
    from datality import AVL
    
    # from datality.bit_mask import BitMask
    from datality import BitMask
    
    # from datality.bst import BST
    from datality import BST
    
    # from datality.deque import Deque
    from datality import Deque
    
    # from datality.disjoint_set import DJS
    from datality import DJS
    
    # from datality.double_linked_list import DoubleLinkedList
    from datality import DoubleLinkedList
    
    # from datality.fenwick_tree import FenwickTree
    from datality import FenwickTree
    
    # from datality.linked_list import LinkedList
    from datality import LinkedList
    
    # from datality.min_heap import Heap
    from datality import Heap
    
    # from datality.radix_trie import RadixTree
    from datality import RadixTree
    
    # from datality.rb_tree import RBTree
    from datality import RBTree
    
    # from datality.segment_tree import SegmentTree
    from datality import SegmentTree
    
    # from datality.skip_list import SkipList
    from datality import SkipList
    
    # from datality.splay_tree import SplayTree
    from datality import SplayTree
    
    # from datality.treap import Treap
    from datality import Treap
    
    # from datality.trie import Trie
    from datality import Trie
    
    # from datality.van_emde_boas import VEB
    from datality import VEB
from bstree import BSTree

def test_get():
    numbers = BSTree()
    numbers.set(1, 'one')
    numbers._invariant()
    numbers.set(2, 'two')
    numbers.set(3, 'three')
    # assert numbers.get('one') == 1


# def test_set():
#     numbers = BSTree()
#     numbers.set('one', 1)
#     assert numbers.get('one') == 1
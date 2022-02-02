class TNode:
    def __init__(self, n):
        self.l = None
        self.r = None
        self.n = n


def same_tree(lnode, rnode):
    if not lnode and not rnode:
        return True

    if (not lnode and rnode) or (lnode and not rnode):
        return False

    is_same = lnode.n == rnode.n

    is_same = is_same and same_tree(lnode.l, rnode.l)

    is_same = is_same and same_tree(lnode.r, rnode.r)

    return is_same

if __name__ == '__main__':
    rt1 = TNode(1)
    rt1.l = TNode(2)
    rt1.r = TNode(3)

    rt1.l.l = TNode(4)
    rt1.l.r = TNode(5)

    rt2 = TNode(1)
    rt2.l = TNode(2)
    rt2.r = TNode(3)

    rt2.l.l = TNode(4)
    rt2.l.r = TNode(6)

    print(same_tree(rt1, rt2))

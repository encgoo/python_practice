
class TNode:
    def __init__(self, n):
        self.l = None
        self.r = None
        self.n = n


def helper(nd):
    ret = []
    if nd.l:
        lst = helper(nd.l)
        lst_new = map(lambda i:([nd.n] + i), lst)
        ret.extend(lst_new)

    if nd.r:
        lst = helper(nd.r)
        lst_new = map(lambda i:([nd.n] + i), lst)
        ret.extend(lst_new)

    if not nd.l and not nd.r:
        return [[nd.n]]

    return ret


def get_sum(root):
    lst = helper(root)
    print(lst)


if __name__ == '__main__':
    root = TNode(1)
    root.l = TNode(2)
    root.r = TNode(3)

    root.l.l = TNode(4)
    root.l.r = TNode(5)

    root.r.l = TNode(6)
    root.r.r = TNode(7)
    get_sum(root)


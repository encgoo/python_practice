
class TNode:
    def __init__(self, n):
        self.l = None
        self.r = None
        self.n = n


def get_leaves(nd, llst):
    if nd.l:
        if not nd.l.l and not nd.l.r:
            llst.append(nd.l.n)
            nd.l = None
        else:
            get_leaves(nd.l, llst)

    if nd.r:
        if not nd.r.l and not nd.r.r:
            llst.append(nd.r.n)
            nd.r = None
        else:
            get_leaves(nd.r, llst)


def get_all_leaves(root):
    ret = []

    nd = root
    while nd.l or nd.r:
        llst = []
        get_leaves(nd, llst)
        ret.append(llst)

    ret.append([nd.n])

    return ret

if __name__ == '__main__':
    root = TNode(1)
    root.l = TNode(2)
    root.r = TNode(3)

    root.l.l = TNode(4)
    root.l.r = TNode(5)

    lst = get_all_leaves(root)
    print(lst)


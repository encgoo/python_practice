from collections import deque

class TNode:
    def __init__(self, n):
        self.l = None
        self.r = None
        self.n = n


class BSTItr:
    def __init__(self, root):
        self.root = root
        self.q = deque()

        nd = root

        while nd:
            self.q.append(nd)
            nd = nd.l

    def has_next(self):
        return len(self.q) == 0

    def next(self):
        p = self.q.pop()
        ret = p.n
        if p.r:
            p = p.r
            while p:
                self.q.append(p)
                p = p.l

        return ret


if __name__ == '__main__':
    root = TNode(8)
    root.l = TNode(3)
    root.r = TNode(10)

    root.l.l = TNode(1)
    root.l.r = TNode(6)

    root.l.r.l = TNode(4)
    root.l.r.r = TNode(7)

    root.r.r = TNode(14)
    root.r.r.l = TNode(13)

    itr = BSTItr(root)

    print(itr.next())
    print(itr.next())
    print(itr.next())
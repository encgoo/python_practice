class TNode:
    def __init__(self, n):
        self.l = None
        self.r = None
        self.n = n


def validate(nd):

    if not nd:
        return True

    is_good = validate(nd.l)
    if nd.l:
        is_good = is_good and nd.l.n < nd.n
    is_good = is_good and validate(nd.r)
    if nd.r:
        is_good = is_good and nd.r.n > nd.n

    return is_good


if __name__=='__main__':
    root = TNode(6)
    root.l = TNode(4)
    root.r = TNode(7)

    root.l.l = TNode(2)
    root.l.r = TNode(5)

    root.l.l.l = TNode(1)
    root.l.l.r = TNode(3)

    root.r.r = TNode(8)

    print(validate(root))

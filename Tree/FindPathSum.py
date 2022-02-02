class TNode:
    def __init__(self, n):
        self.l = None
        self.r = None
        self.n = n


def find_sum(node, cur, trgt):
    if not node.l and not node.r:
        return cur + node.n == trgt

    ret = False
    if node.l:
        ret = ret or find_sum(node.l, cur + node.n, trgt)
    if node.r:
        ret = ret or find_sum(node.r, cur + node.n, trgt)

    return ret


if __name__ == '__main__':
    root = TNode(1)

    root.l = TNode(2)
    root.r = TNode(3)

    root.l.l = TNode(4)
    root.l.r = TNode(5)

    root.r.l = TNode(6)

    root.l.l.l = TNode(7)

    print(find_sum(root, 0, 25))
from collections import deque

class TNode:
    def __init__(self, n):
        self.l = None
        self.r = None
        self.n = n


def invert(node):
    if not node:
        return

    node.l, node.r = node.r, node.l

def print_level(node):
    c = deque()
    n = deque()

    c.append(node)
    while c:
        q = c.popleft()
        print(q.n, end='')
        if q.l:
            n.append(q.l)
        if q.r:
            n.append(q.r)

        if not c:
            print('')
            c, n = n, c

if __name__ == '__main__':
    root = TNode(1)

    root.l = TNode(2)
    root.r = TNode(3)

    root.l.l = TNode(4)
    root.l.r = TNode(5)

    root.r.l = TNode(6)

    root.l.l.l = TNode(7)

    print_level(root)
    invert(root)
    print_level(root)
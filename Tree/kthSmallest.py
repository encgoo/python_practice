from collections import deque

class TNode:
    def __init__(self, n):
        self.l = None
        self.r = None
        self.n = n


def find(node, q, k):
    if len(q) > k:
        return None

    # dfs
    ret = None
    if node.l:
        ret = find(node.l, q, k)

    if ret:
        return ret

    if len(q) == k - 1:
        q.append(node.n)
        return node.n
    else:
        q.append(node.n)

    if node.r:
        ret = find(node.r, q, k)

    return ret


def find_kth(root, k):
    q = deque()
    ret = find(root, q, k)
    return ret

if __name__ == '__main__':
    root = TNode(6)
    root.l = TNode(4)
    root.r = TNode(7)

    root.l.l = TNode(2)
    root.l.r = TNode(5)

    root.l.l.l = TNode(1)
    root.l.l.r = TNode(3)

    root.r.r = TNode(8)

    print(find_kth(root, 10))







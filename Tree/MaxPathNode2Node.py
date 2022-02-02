import sys

class TNode:
    def __init__(self, n):
        self.l = None
        self.r = None
        self.n = n


def get_max(nd):
    if not nd:
        return 0, -sys.maxsize
    u_sum = nd.n

    u_sum1 = 0
    p_sum1 = -sys.maxsize
    if nd.l:
        u_sum1, p_sum1 = get_max(nd.l)

    u_sum2 = 0
    p_sum2 = -sys.maxsize
    if nd.r:
        u_sum2, p_sum2 = get_max(nd.r)

    u_sum += max(u_sum1, u_sum2)
    p_sum = max(p_sum1, p_sum2)
    p_sum = max(p_sum, u_sum1 + u_sum2 + nd.n)

    return u_sum, p_sum

if __name__ == '__main__':
    root = TNode(1)
    root.l = TNode(2)
    root.r = TNode(3)

    print(get_max(root))
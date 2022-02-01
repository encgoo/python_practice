from collections import deque

class TNode:
    def __init__(self, n):
        self.l = None
        self.r = None
        self.n = n

    # dfs has preorder, inorder, and postorder
    def preorder(self):
        print(self.n, end=',')
        if self.l:
            self.l.preorder()
        if self.r:
            self.r.preorder()

    def inorder(self):
        if self.l:
            self.l.inorder()
        print(self.n, end=',')

        if self.r:
            self.r.inorder()

    def postorder(self):
        if self.l:
            self.l.postorder()
        if self.r:
            self.r.postorder()
        print(self.n, end=',')

    # bfs
    def bfs(self):
        q = deque()
        q.append(self)

        while q:
            p = q.popleft()
            print(p.n, end=',')
            if p.l:
                q.append(p.l)
            if p.r:
                q.append(p.r)

    def level(self):
        c = deque()
        n = deque()

        c.append(self)

        while c:
            p = c.popleft()
            print(p.n, end='')
            if p.l:
                n.append(p.l)
            if p.r:
                n.append(p.r)

            if not c:
                print('')
                c, n = n, c

    def level2(self):
        q = deque()
        c = deque()
        n = deque()

        c.append(self)

        lst = []
        while c:
            p = c.popleft()
            lst.append(p.n)

            if p.l:
                n.append(p.l)
            if p.r:
                n.append(p.r)

            if not c:
                q.append(lst)
                lst = []
                c, n = n, c

        while q:
            p = q.pop()
            print(p)


if __name__ == '__main__':
    root = TNode(1)

    root.l = TNode(2)
    root.r = TNode(3)

    root.l.l = TNode(4)
    root.l.r = TNode(5)

    root.r.l = TNode(6)

    root.l.l.l = TNode(7)

    print('')
    root.inorder()
    print('')
    root.preorder()
    print('')
    root.postorder()
    print('')
    root.bfs()
    print('')

    root.level()

    print('')
    root.level2()
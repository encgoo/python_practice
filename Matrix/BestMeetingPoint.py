import sys


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, i, j):
        return abs(self.x - i) + abs(self.y - j)


def find_houses(m):
    num_y = len(m)
    num_x = len(m[0])

    ret = []
    for i in range(num_y):
        for j in range(num_x):
            if m[i][j] == 1:
                p = point(j, i)
                ret.append(p)

    return ret


def find_total(x, y, houses):
    num_h = len(houses)

    dist = 0
    for i in range(num_h):
        h = houses[i]
        dist += h.dist(x, y)

    return dist


def find_meeting_point(m):
    num_y = len(m)
    num_x = len(m[0])
    houses = find_houses(m)

    ret = sys.maxsize
    for i in range(num_y):
        for j in range(num_x):
            if m[i][j] == 0:
                ret = min(ret, find_total(j, i, houses))

    return ret


if __name__ == '__main__':
    m = [
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]

    print(find_meeting_point(m))

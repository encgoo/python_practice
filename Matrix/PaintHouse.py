import sys


def print_house(clrs, i, j, rec):
    if rec[j][i] != -1:
        return rec[j][i]

    num_c = len(clrs)
    num_h = len(clrs[0])

    ret = sys.maxsize

    for k in range(num_c):
        if k != j:
            cur = clrs[k][i]
            if i < num_h - 1:
                cur += print_house(clrs, i + 1, k, rec)
            ret = min(ret, cur)

    rec[j][i] = ret
    return ret


def find_min(clrs):
    num_c = len(clrs)
    num_h = len(clrs[0])
    ret = sys.maxsize

    for c in range(num_c):
        rec = [[-1]*num_h for _ in range(num_c)]
        ret = min(ret, print_house(clrs, 0, c, rec))

    return ret


if __name__ == '__main__':
    m = [
        [1,2,3,4],
        [5,6,2,3],
        [10,8,9,6]
    ]

    print(find_min(m))
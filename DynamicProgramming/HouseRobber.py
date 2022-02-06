
def get_max(mlst):
    sz = len(mlst)
    rob = mlst[0]
    skip = 0

    for i in range(1, sz):
        rob_i = mlst[i] + skip
        skip_i = max(rob, skip)
        rob = rob_i
        skip = skip_i

    return max(rob, skip)


def find_max(mlst):
    sz = len(mlst)
    mem = [(0,0) for _ in range(sz)]

    mem[0] = (mlst[0], 0)

    for i in range(1, len(mlst)):
        rob_i = mlst[i] + mem[i-1][1]
        skip_i = max(mem[i-1][0], mem[i-1][1])
        mem[i] = (rob_i, skip_i)

    return max(mem[sz - 1][0], mem[sz - 1][1])


if __name__ == '__main__':
    lst = [50, 1, 6, 10, 1, 2, 3, 50]

    print(find_max(lst))
    print(get_max(lst))
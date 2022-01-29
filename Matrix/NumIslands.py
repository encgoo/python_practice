# A matrix of mxn with value 0 or 1. Find islands denoted by 1.


def find_connected(m, visited, i, j):

    if m[i][j] == 0 or visited[i][j]:
        return

    num_r = len(m)
    num_c = len(m[0])
    visited[i][j] = True
    m[i][j] = 2

    if i + 1 < num_r:
        find_connected(m, visited, i + 1, j)

    if i - 1 > 0:
        find_connected(m, visited, i - 1, j)

    if j + 1 < num_c:
        find_connected(m, visited, i, j + 1)

    if j - 1 > 0:
        find_connected(m, visited, i, j - 1)


def count_island(m):

    num_r = len(m)
    num_c = len(m[0])
    cnt = 0
    for i in range(num_r):
        for j in range(num_c):
            if m[i][j] == 1:
                cnt += 1
                visited = [[False]*num_c for _ in range(num_r)]
                find_connected(m, visited, i, j)

    return cnt


if __name__ == '__main__':
    m = [
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,1,0]
    ]
    print(count_island(m))


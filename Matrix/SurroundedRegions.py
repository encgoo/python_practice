
def is_free(m, visited, i, j):
    if m[i][j] == 0:
        # this direction is blocked
        return False

    num_r = len(m)
    num_c = len(m[0])
    # use 2 for a free block
    if i == 0 or i == num_r - 1 or j == 0 or j == num_c - 1 or m[i][j] == 2:
        return True

    # use 3 for a captured block
    if m[i][j] == 3:
        return False

    visited[i][j] = True
    free_blk = False
    if not visited[i + 1][j]:
        free_blk = free_blk or is_free(m, visited, i + 1, j)
    if not visited[i - 1][j]:
        free_blk = free_blk or is_free(m, visited, i - 1, j)
    if not visited[i][j+1]:
        free_blk = free_blk or is_free(m, visited, i, j + 1)
    if not visited[i][j-1]:
        free_blk = free_blk or is_free(m, visited, i, j - 1)

    if free_blk:
        m[i][j] = 2
    else:
        m[i][j] = 3

    return free_blk


def count_captured(m):
    num_r = len(m)
    num_c = len(m[0])

    cnt = 0
    for i in range(num_r):
        for j in range(num_c):
            if m[i][j] == 1:
                visited = [[False]*num_c for _ in range(num_r)]
                if not is_free(m, visited, i, j):
                    cnt += 1

    return cnt


if __name__ == '__main__':
    m = [
        [0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0]
    ]
    print(count_captured(m))
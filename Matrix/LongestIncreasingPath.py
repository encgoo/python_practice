
def find_path(m, rec, i, j):
    num_r = len(m)
    num_c = len(m[0])

    if rec[i][j] != 0:
        return rec[i][j]

    # at least 1
    rec[i][j] = 1

    additional = 0
    if i - 1 >= 0 and m[i-1][j] > m[i][j]:
        additional = max(additional, find_path(m, rec, i - 1, j))

    if i + 1 < num_r and m[i + 1][j] > m[i][j]:
        additional = max(additional, find_path(m, rec, i + 1, j))

    if j - 1 >= 0 and m[i][j -1] > m[i][j]:
        additional = max(additional, find_path(m, rec, i, j - 1))

    if j + 1 < num_c and m[i][j + 1] > m[i][j]:
        additional = max(additional, find_path(m, rec, i, j + 1))

    rec[i][j] += additional

    return rec[i][j]


def longest_path(m):
    num_r = len(m)
    num_c = len(m[0])

    rec = [[0]*num_c for _ in range(num_r)]

    for i in range(num_r):
        for j in range(num_c):
            if rec[i][j] == 0:
                find_path(m, rec, i, j)

    return rec

if __name__ == '__main__':
    m = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]

    print(longest_path(m))

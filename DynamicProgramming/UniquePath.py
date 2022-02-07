
def unique_paths(m, n):
    cnt = [[0]*m for _ in range(n)]

    # can only going right
    for i in range(m):
        cnt[n-1][i] = 1

    # can only going down
    for i in range(n):
        cnt[i][m-1] = 1

    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            cnt[i][j] = cnt[i+1][j] + cnt[i][j+1]

    return cnt[0][0]


if __name__ == '__main__':
    print(unique_paths(1, 100))
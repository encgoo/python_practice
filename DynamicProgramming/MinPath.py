
def min_path(m):

    num_r = len(m)
    num_c = len(m[0])
    if num_r == 0 or num_c == 0:
        return 0

    sum = [[0]*num_c for _ in range(num_r)]

    # init the last row
    sum[num_r-1][num_c-1] = m[num_r-1][num_c-1]
    p = num_c-2
    last_r = num_r - 1
    while p >= 0:
        sum[last_r][p] = sum[last_r][p+1] + m[last_r][p]
        p -= 1

    # init the last column
    last_c = num_c - 1
    r = num_r - 2
    while r >= 0:
        sum[r][last_c] = sum[r + 1][last_c] + m[r][last_c]
        r -= 1

    r = num_r - 2
    while r >= 0:
        c = num_c -2
        while c >= 0:
            sum[r][c] = m[r][c] + min(sum[r + 1][c], sum[r][c + 1])
            c -= 1
        r -= 1

    return sum[0][0]


if __name__=='__main__':
    print(min_path([[1,2,3], [1,5,8]]))
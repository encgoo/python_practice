
def find_perfect_square(n):
    rec = [0]*(n+1)

    # 1 is a perfect square.
    for j in range(n+1):
        rec[j] = j

    lmt = int(n**0.5)
    for i in range(2, lmt+1):
        sqr = i*i

        max_count = int(n/sqr) + 1
        for k in range(1, max_count):
            for j in range(k*sqr, n+1):
                rec[j] = min(rec[j], rec[j-k*sqr]+k)

    return rec[n]

if __name__ == '__main__':
    print(find_perfect_square(15))

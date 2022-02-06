

def check(lst):
    sz = len(lst)
    rec = [False]*sz
    rec[0] = 1
    for i in range(sz):
        if rec[sz - 1]:
            break
        if not rec[i]:
            continue

        if lst[i] != 0:
            for j in range(1, lst[i] + 1):
                rec[i + j] = True

    return rec[sz-1]

if __name__ == '__main__':
    print(check([2,3,1,1,4]))
    print(check([3,2,1,0, 4]))

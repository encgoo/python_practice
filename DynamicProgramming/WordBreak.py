

# The key point here is that the word set is small. Then it is like the coin change problem.
# Use all the words in the give word set as available coin change.

# if we don't have the word set, but a real dict, can we still use the same approach?

def is_word(w):
    if w == 'cat' or w == 'a' or w == 'at':
        return True
    return False


def find_next(mem, n):
    for i in range(n, len(mem)):
        if mem[i]:
            return i + 1
    return -1


def get_sentence(clst):

    sz = len(clst)
    mem = [[] for _ in range(sz)]

    st = 0
    while st != -1 and st < sz:
        for i in range(st, len(clst)):
            wd = clst[st:i + 1]
            if is_word(wd):
                if st-1 != 0:
                    mem[i].extend(mem[st-1])
                mem[i].append(wd)
        if mem[sz - 1]:
            break

        st = find_next(mem, st)

    return mem[sz-1]


if __name__ == '__main__':
    clst = 'atacatcat'
    print(get_sentence(clst))




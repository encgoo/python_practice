# In computer science, edit distance is a way of quantifying how dissimilar two strings (e.g., words) are to one another
# by counting the minimum number of operations required to transform one string into the other.


def min_dist(w1, w2):
    sz1 = len(w1)
    sz2 = len(w2)

    mem = [[-1]*sz2 for _ in range(sz1)]

    return find_dist(w1, w2, mem, sz1-1, sz2-1)


def find_dist(w1, w2, mem, i, j):
    if i < 0:
        return j + 1
    elif j < 0:
        return i + 1

    if mem[i][j] != -1:
        return mem[i][j]

    if w1[i] == w2[j]:
        mem[i][j] = find_dist(w1, w2, mem, i - 1, j - 1)
    else:
        # delete and insert has the same effect regarding counting.
        # this is deleting from w1 or w2
        preMin = min(find_dist(w1, w2, mem, i, j - 1), find_dist(w1, w2, mem, i-1, j))
        # this is for replacing
        preMin = min(preMin, find_dist(w1, w2, mem, i-1, j-1))
        mem[i][j] = 1 + preMin

    return mem[i][j]


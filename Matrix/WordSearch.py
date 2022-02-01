

def search_word(lst, i, j, wrd, k, visited):
    num_w = len(lst)
    num_c = len(lst[0])
    if k == len(wrd) - 1:
        if wrd[k] == lst[i][j]:
            return True
        else:
            return False

    if wrd[k] != lst[i][j]:
        return False

    is_good = False
    visited[i][j] = True
    if i + 1 < num_w and not visited[i+1][j]:
        is_good = search_word(lst, i + 1, j, wrd, k+1, visited)

    if i - 1 > 0 and not visited[i-1][j]:
        is_good = is_good or search_word(lst, i - 1, j, wrd, k+1, visited)

    if j + 1 < num_c and not visited[i][j + 1]:
        is_good = is_good or search_word(lst, i, j + 1, wrd, k + 1, visited)

    if j - 1 > 0 and not visited[i][j - 1]:
        is_good = is_good or search_word(lst, i, j - 1, wrd, k + 1, visited)

    return is_good


def word_search(lst, wrd):
    num_w = len(lst)
    num_c = len(lst[0])

    found = False
    for i in range(num_w):
        for j in range(num_c):
            visited = [[False]*num_c for _ in range(num_w)]
            found = search_word(lst, i, j, wrd, 0, visited)
            if found:
                break
        if found:
            break

    return found

if __name__ == '__main__':
    m = [
        'ABCE',
        'SFCS',
        'ADEE'
    ]

    print(word_search(m, 'ABCCED'))
    print(word_search(m, 'SEE'))
    print(word_search(m, 'ABCB'))



# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26


def get_char(num_str):
    return chr(int(num_str) - 1 + ord('A'))


def decode(lst):
    sz = len(lst)
    rec = [[] for _ in range(sz)]

    rec[0].append(get_char(lst[0]))
    rec[1].append(get_char(lst[0]) + get_char(lst[1]))
    if int(lst[:2]) <= 26:
        rec[1].append(get_char(lst[:2]))

    idx = 2
    while idx < sz:
        possible1 = rec[idx - 1]
        for s in possible1:
            # used alone
            rec[idx].append(s + get_char(lst[idx]))
        num_str = lst[idx - 1] + lst[idx]
        if int(num_str) <= 26:
            possible2 = rec[idx - 2]
            for s in possible2:
                rec[idx].append(s + get_char(num_str))

        idx += 1

    return rec[sz - 1]


if __name__ == '__main__':
    print(decode('85121215'))

def max_profit(prcs):
    # keep track of best buy so far, and profit
    max_profit = 0
    buy = prcs[0]
    sz = len(prcs)

    for i in range(1, sz):
        # if sell now
        max_profit = max(max_profit, prcs[i] - buy)
        buy = min(prcs[i], buy)

    return max_profit

if __name__ == '__main__':
    ps =[3,1, 6, 9, 10, 5, 6]
    print(max_profit(ps))
    print(max_profit([3,2,1]))


import numpy as np

# S0: price of stock at t = 0
# k: Strike price of the option
# r: risk free interest rate
# u: up rate
# d: down rate
def binomialModel(s0, u, d, t, k, r):
    stockVals = np.zeros((t + 1, t + 1))
    optionVals = np.zeros((t + 1, t + 1))

    stockVals[0, 0] = s0

    for i in range(1, t + 1):
        stockVals[i, 0] = stockVals[i - 1, 0] * u
        for j in range(1, i + 1):
            stockVals[i, j] = stockVals[i - 1, j - 1] * d

    # Last level of tree
    for j in range(t + 1):
        optionVals[t, j] = max(0, stockVals[t, j] - k)

    # Backward loop to get C0
    for i in range(t - 1, -1, -1):
        for j in range(i + 1):
            optionVals[i, j] = calculateCo(u, d, r, optionVals[i + 1, j], optionVals[i + 1, j + 1])
            # optionVals[i, j] = calculateCo(stockVals[i,j], u, d, r, optionVals[i + 1, j], optionVals[i + 1, j + 1])

    print(stockVals)
    print('\n')
    print(optionVals)
    return optionVals[0, 0]


def calculateCo(u, d, r, cu, cd):
    p = ((1+r)-d) / (u-d)
    c = (p*cu + (1-p)*cd) / (1+r)
    return c


if __name__ == '__main__':
    x = binomialModel(80, 1.5, 0.5, 3, 80, 0.1)   # == 34
    print('---------------------')
    print(f'C0 = {x}')

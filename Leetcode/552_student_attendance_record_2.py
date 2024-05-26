
MOD = 1000000000 + 7

# Bruteforce
def checkRecord(n: int) -> int:
    return numPossibleRecords(n, 1, 2)

def numPossibleRecords(n: int, numAbsensesRemaining: int, numLatesRemaining: int) -> int:
    if n == 0:
        return 1
    total = 0

    # Pick P
    total += numPossibleRecords(n - 1, numAbsensesRemaining, 2)

    if numAbsensesRemaining > 0:
        # Pick A
        total += numPossibleRecords(n - 1, numAbsensesRemaining - 1, 2)
        total %= MOD

    if numLatesRemaining > 0:
        # Pick L
        total += numPossibleRecords(n - 1, numAbsensesRemaining, numLatesRemaining - 1)
        total %= MOD

    return total



# Memoization
def checkRecord2(n: int) -> int:
    prevDP = [[1] * 3 for _ in range(2)]

    for i in range(1, n + 1):
        newDP = [[0] * 3 for _ in range(2)]
        for a in range(2):
            for l in range(3):
                # Pick P
                newDP[a][l] += prevDP[a][2]
                newDP[a][l] %= MOD
                if a > 0:
                    # Pick A
                    newDP[a][l] += prevDP[a - 1][2]
                    newDP[a][l] %= MOD
                if l > 0:
                    # Pick L
                    newDP[a][l] += prevDP[a][l - 1]
                    newDP[a][l] %= MOD
        prevDP = newDP

    return prevDP[1][2]

assert checkRecord2(10101) == 183236316
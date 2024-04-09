def grid_traveler(m, n, memo={}):
    key = str(m) + ',' + str(n)

    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[key] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
    return memo[key]


assert grid_traveler(1,1) == 1
assert grid_traveler(2,3) == 3
assert grid_traveler(3,3) == 6
assert grid_traveler(18, 18) == 2333606220

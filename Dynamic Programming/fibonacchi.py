# Memoization
def fib(num, memo={}):
    if num in memo:
        return memo[num]
    if num <= 2:
        return num
    memo[num] = fib(num - 1, memo) + fib(num - 2, memo)
    return memo[num]

print(fib(100))
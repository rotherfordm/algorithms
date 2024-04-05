def minSubArrayLen(target, nums):
    l, total = 0, 0
    res = float("inf")
    for r in range(len(nums)):
        total += nums[r]

        while total >= target:
            res = min(r - l + 1, res)
            total -= nums[l]
            l += 1

    return 0 if res == float("inf") else res


assert minSubArrayLen(7, [2,3,1,2,4,3]) == 2
def removeDuplicates(nums) -> int:
    least = float('-inf')
    p1 = 0

    for i in range(len(nums)):
        if nums[i] > least:
            least = nums[i]
            nums[p1] = nums[i]
            p1 += 1

    for i in range(p1, len(nums)):
        nums.pop()

    return nums

assert removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == [0,1,2,3,4]
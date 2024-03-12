def removeElement(nums, val):
    replaced = 0
    k = 0
    for i, num in enumerate(nums):
        if num == val:
            nums[i] = "_"
            replaced += 1
        else:
            k += 1

    nums = [i for i in nums if i != "_"] + ["_" for i in range(0, replaced)]

    print(k, nums, replaced)
    return k


print(removeElement([0,1,2,2,3,0,4,2], 2))
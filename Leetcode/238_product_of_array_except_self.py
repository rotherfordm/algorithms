import math

def productExceptSelf(nums):
    products = []
    prev_num = None
    prev_pos = None

    for i in range(0, len(nums)):
        if isinstance(prev_num, int):
            nums[prev_pos] = prev_num

        prev_pos = i
        prev_num = nums[i]
        nums[i] = 1
        products.append(math.prod(nums))

    return products

def productExceptSelf2(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


print(productExceptSelf2([1,2,3,4]))
print(productExceptSelf2([-1,1,0,-3,3]))

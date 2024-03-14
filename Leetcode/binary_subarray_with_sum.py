def numSubarraysWithSum(nums, goal):
    left1 = left2 = sum1 = sum2 = idx = total_subarrays = 0
    array_length = len(nums)

    # Iterate over the array to find subarrays with sum equal to goal
    while idx < array_length:
        # Increase running sums with the current number
        sum1 += nums[idx]
        sum2 += nums[idx]

        # Decrease sum1 until it's no more than goal by moving left1 pointer right
        while left1 <= idx and sum1 > goal:
            sum1 -= nums[left1]
            left1 += 1

        # Decrease sum2 until it's just less than goal by moving left2 pointer right
        while left2 <= idx and sum2 >= goal:
            sum2 -= nums[left2]
            left2 += 1

        # Add the number of new subarrays found to the total
        total_subarrays += left2 - left1

        # Move to the next element
        idx += 1

    return total_subarrays


print(numSubarraysWithSum([1,0,1,0,1], 2))
print(numSubarraysWithSum([0,0,0,0,0], 0))
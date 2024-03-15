# O(nLogn) time | O(n) space
def sortedSquares1(nums):
    sortedSqres = [0 for _ in nums]

    for idx in range(len(nums)):
        value = nums[idx]
        sortedSqres[idx] = value * value

    sortedSqres.sort()
    return sortedSqres


def sortedSquares2(nums):
    sortedSqres = [0 for _ in nums]

    smallerValueIdx = 0
    largerValueIdx = len(nums) -1

    for idx in reversed(range(len(nums))):
        smallerValue = nums[smallerValueIdx]
        largerValue = nums[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSqres[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSqres[idx] = largerValue * largerValue
            largerValueIdx -= 1

    return sortedSqres


# print(sortedSquares1([-4,-1,0,3,10]))
print(sortedSquares2([-4,-1,0,3,10]))
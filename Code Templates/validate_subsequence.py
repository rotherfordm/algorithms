# O(n) time | O(1) space
def validateSubsequence1(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

def validateSubsequence2(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx+=1
    return seqIdx == len(sequence)


print(validateSubsequence1([1,2,3,4,5], [2,3]))
print(validateSubsequence2([1,2,3,4,5], [2,3]))

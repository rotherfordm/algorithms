def isSubsequence(s, t):
    sequence = list(s)
    array = list(t)

    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

assert isSubsequence("abc", "ahbgdc") == True
assert isSubsequence("axc", "ahbgdc") == False
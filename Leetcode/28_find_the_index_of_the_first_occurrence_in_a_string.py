def strStr(haystack, needle):
    i = 0
    j = 0

    while True:
        while True:
            if j == len(needle):
                return i
            if i + j == len(haystack):
                return -1
            if needle[j] != haystack[i + j]:
                break
            j += 1

        i += 1
        j = 0


print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
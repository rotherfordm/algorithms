def longestCommonPrefix(strs):
    strs.sort(key=len)
    temp_str = strs[0]

    if not temp_str:
        return ""

    for i in range(1, len(strs)):
        for k in range(0, len(temp_str)):
            if temp_str[k] != strs[i][k]:
                temp_str = temp_str[0:k]
                break

        if not temp_str:
            return temp_str

    return temp_str

assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
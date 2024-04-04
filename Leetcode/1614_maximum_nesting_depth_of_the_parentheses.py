def maxDepth(s):
    count = 0
    max_count = 0

    for char in s:
        if char == "(":
            count += 1
        if count > max_count:
            max_count = count
        if char == ")":
            count -= 1

    return max_count

assert maxDepth("(1+(2*3)+((8)/4))+1") == 3
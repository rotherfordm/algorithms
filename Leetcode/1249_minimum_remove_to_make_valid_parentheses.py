def minRemoveToMakeValid(s: str) -> str:
    stack = []
    count = 0

    for char in s:
        if char == "(":
            stack.append(char)
            count += 1
        elif char == ")" and count > 0:
            stack.append(char)
            count -= 1
        elif char != ")":
            stack.append(char)

    filtered = []
    for char in stack[::-1]:
        if char == "(" and count > 0:
            count -= 1
        else:
            filtered.append(char)

    return "".join(filtered[::-1])

assert minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
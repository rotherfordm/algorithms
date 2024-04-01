def lengthOfLastWord(s):
    count = 0
    prev = " "
    for i in range(len(s) - 1, -1, -1):
        if s[i] == " " and prev != " ":
            return count
        if s[i] != " ":
            count += 1
        prev = s[i]
    return count

assert lengthOfLastWord("Hello World") == 5
assert lengthOfLastWord("   fly me   to   the moon  ") == 4
assert lengthOfLastWord("luffy is still joyboy") == 6

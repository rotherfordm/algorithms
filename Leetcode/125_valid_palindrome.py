def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while (i < j):
        while (i < j and not (s[i].isdigit() or s[i].isalpha())):
            i = i + 1
        while (i < j and not (s[j].isdigit() or s[j].isalpha())):
            j = j - 1
        if s[i].lower() != s[j].lower():
            return False
        i = i + 1
        j = j - 1
    return True
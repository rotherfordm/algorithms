def isPalindrome(self, x: int) -> bool:
    # Two pointers
    arr = str(x)
    l = 0
    r = len(arr) - 1

    while (l < r):
        if arr[l] != arr[r]:
            return False
        l += 1
        r -= 1
    return True
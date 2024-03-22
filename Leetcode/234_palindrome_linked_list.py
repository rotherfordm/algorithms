def isPalindrome(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next

    i = 0
    j = len(vals) - 1
    while (i < j):
        if vals[i] != vals[j]:
            return False
        i += 1
        j -= 1

    return True
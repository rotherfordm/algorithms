class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1, l2):
    def reverseList(head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    ordered_l1 = reverseList(l1)
    ordered_l2 = reverseList(l2)

    list_1 = []
    while ordered_l1:
        list_1.append(str(ordered_l1.val))
        ordered_l1 = ordered_l1.next

    list_2 = []
    while ordered_l2:
        list_2.append(str(ordered_l2.val))
        ordered_l2 = ordered_l2.next

    val1 = int("".join(list_1))
    val2 = int("".join(list_2))

    total = str(val1 + val2)

    newList = ListNode()
    newList.val = total[-1]

    curr = newList
    for i in range(len(total) - 2, -1, -1):
        list_insert = ListNode()
        list_insert.val = int(total[i])
        curr.next = list_insert
        curr = curr.next

    return newList
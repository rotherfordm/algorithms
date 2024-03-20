def merge(list1, a, b, list2):
    curr = list1
    i = 0
    while i < a - 1:
        curr = curr.next
        i += 1

    head = curr
    while i <= b:
        curr = curr.next
        i += 1
    head.next = list2

    while list2.next:
        list2 = list2.next
    list2.next = curr
    return list1

print(merge([10,1,13,6,9,5], 3, 4, [1000000,1000001,1000002]))
from collections import deque

def timeRequiredToBuy(tickets, k):
    count = 0

    q = deque()
    for i in range(len(tickets)):
        q.append(i)

    while q:
        count += 1
        curr = q.popleft()
        tickets[curr] -= 1

        if k == curr and tickets[curr] == 0:
            return count

        if tickets[curr] != 0:
            q.append(curr)

    return count

def timeRequiredToBuy2(tickets, k) -> int:
    total = 0
    for elem in tickets[:k + 1]:
        total += elem if elem <= tickets[k] else tickets[k]

    for elem in tickets[k + 1:]:
        total += elem if elem < tickets[k] else tickets[k] - 1

    return total

def timeRequiredToBuy3(tickets, k) -> int:
    total = 0
    for elem in tickets[:k + 1]:
        if elem <= tickets[k]:
            total += elem
        else:
            total += tickets[k]

    for elem in tickets[k + 1:]:
        if elem < tickets[k]:
            total += elem
        else:
            total += tickets[k] - 1
    return total

assert timeRequiredToBuy([2,3,2], 2) == 6
assert timeRequiredToBuy2([2,3,2], 2) == 6
assert timeRequiredToBuy3([2,3,2], 2) == 6

print(timeRequiredToBuy3([5,1,1,1], 1))
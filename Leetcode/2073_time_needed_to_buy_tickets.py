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

assert timeRequiredToBuy([2,3,2], 2) == 6
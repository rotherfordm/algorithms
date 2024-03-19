from collections import Counter, deque
import heapq

def task_scheduler(tasks, n):
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque()

    while maxHeap or q:
        time += 1
        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])
    return time

print(task_scheduler(["A","A","A","B","B","B"], 2))
print(task_scheduler(["A","C","A","B","D","B"], 1))

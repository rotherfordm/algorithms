def merge(intervals):
    intervals.sort()

    prev = intervals[0]
    new_intervals = []

    if len(intervals) == 1:
        return intervals

    for i in range(1, len(intervals)):
        curr = intervals[i]

        if curr[0] <= prev[1]:
            prev = [min(prev[0], curr[0]), max((prev[1], curr[1]))]
        else:
            new_intervals.append(prev)
            prev = curr

    if prev:
       new_intervals.append(prev)

    return new_intervals




print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,3]]))
print(merge([[1,4],[5,6]]))
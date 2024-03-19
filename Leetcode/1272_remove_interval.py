def remove_interval(intervals, to_remove):
    intervals.sort()

    res = []
    for i in range(0, len(intervals)):
        current = intervals[i]

        # check if overlapping
        if to_remove[0] <= current[1]:
            print([min(current[0], to_remove[0]), min(current[1], to_remove[0])])
            # res.append([])





print(remove_interval([[0, 2], [3, 4], [5, 7]], [1, 6]))  # [[0, 1], [6,7]]
# print(remove_interval([[0, 5]], [2, 3]))  # [[0,2], [3, 5]]
# print(remove_interval([[-1, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], [-1, 4]))  # [[-5, -4], [-3, -2], [4, 5], [8, 9]]

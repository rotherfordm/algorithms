"""Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It’s
much less efficient on large lists than more advanced algorithms like quicksort, heapsort, or merge sort. Still,
it provides several advantages such as it’s easy to understand the algorithm, it performs well with small lists or
lists that are already partially sorted and it can sort the list as it receives it. The algorithm iterates,
consuming one input element each repetition and growing a sorted output list. At each iteration, it removes one
element from the input data, finds the location it belongs within the sorted list and inserts it there. It repeats
until no input elements remain.

Implementation: https://www.geeksforgeeks.org/insertion-sort
"""


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        # print(i)

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        print("--")
        print(j)
        print(arr[j])
        while j >= 0 and key < arr[j]:
            print("inner while", j)
            arr[j + 1] = arr[j]
            j -= 1
        print("--")
        arr[j + 1] = key


def test_function():
    # Driver code to test above
    test_arr = [12, 11, 13, 5, 6]
    insertion_sort(test_arr)

    for i in range(len(test_arr)):
        print("% d" % test_arr[i])


test_function()

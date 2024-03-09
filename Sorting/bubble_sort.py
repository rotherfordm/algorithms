"""Bubble Sort is a simple sorting algorithm that works by repeatedly swapping the adjacent elements if they are in
the wrong order. It gets its name because with each iteration the largest element “bubbles” up to its proper
location. It continues this process of swapping until the entire list is sorted in ascending order. The main steps of
the algorithm are: starting from the beginning of the list, compare every pair of adjacent items and swap them if
they are in the wrong order, and then pass through the list until no more swaps are needed. However, despite being
simple, Bubble Sort is not suited for large datasets as it has a worst-case and average time complexity of O(n²),
where n is the number of items being sorted."""

def bubbleSort(arr):
  n = len(arr)
  # optimize code, so if the array is already sorted,
  # it doesn't need to go through the entire process

  swapped = False

  # Traverse through all array elements
  for i in range(n-1):
    # print(i)
    # range(n) also works but outer loop will
    # repeat one time more than needed.
    # Last i elements are already in place

    for j in range(0, n-i-1):
      # print(i, j)
      # traverse the array from to n-i-1
      # Swap if the element found is greater
      # than the next element
      if arr[j] > arr[j + 1]:
        swapped = True
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # arr[j] = arr[j+1]
        # arr[j+1] = arr[j]

    if not swapped:
      # if we haven't needed to make a single swap, we
      # can just exit the main loop.
      return






arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
  print("% d" % arr[i], end=" ")
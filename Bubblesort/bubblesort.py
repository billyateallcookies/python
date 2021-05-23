"""
Basic Bubblesort program.
"""

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n 0 - i - 1
            # swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
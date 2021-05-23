"""
Basic Timsort program.
"""

min_merge = 32


def calc_min_run(n):
    """
    Returns the minimum length of a run from 23 - 64 so that the
    len(array)/minrun is less than or equal to  a power of 2.
    
    1 => 1, ..., 63 => 63, 64 => 32, 65 => 33, ..., 127 => 64, 
    128 => 32, ...
    """

    r = 0
    while n >= min_merge:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(arr, left ,right):
    """
    Sorts array from left index to right index
    which is of size atmost run.
    """

    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def merge(arr, l, m, r):
    """
    Merges the sorted runs.
    """

    # original array is broken in to two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    
    i, j, k = 0, 0, l

    # after comparing, we merge those two arrays,
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        
        k += 1
    
    # Copy remaining elements from left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        j += 1
    
    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def timsort(_arr):
    """
    Iterative Timsort function to sort the array[0...n-1] 
    (similar to merge sort)
    """
    arr = _arr

    n = len(arr)
    min_run = calc_min_run(n)

    # Sort individual subarrays of size run.
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # Sort merging from size run (or 32). It will merge to
    # form size 64,  then 128, 256 and so on...
    size = min_run
    while size < n:
        # Pick starting point of left sub array.
        # merge arr[left...left+size-1] and arr[left+size, left+2*size-1]
        # after every merge, increase left by 2 * size
        for left in range(0, n, 2 * size):
            # find ending point off left sub array
            # mid + 1 is the starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub array arr[left...mid] & arr[mid+1...right]
            if mid < right:
                merge(arr, left, mid, right)
            
        size = 2 * size
    
    return arr



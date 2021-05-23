"""
Basic Heapsort program.
"""

def heapify(arr, n, i):
    """
    Heapifies subtree rooted at index i
    n - size of the heap
    """

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # see if left child of root exists and is 
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
    
    # see if right child of root exists and is 
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    # change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # heapift the root
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # build a maxheap
    for i in range(n // 2 -1, -1, -1):
        heapify(arr, n, i)
    
    # extract the elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr
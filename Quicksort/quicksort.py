"""
Basic Quicksort program.
"""

def partition(start, end, array):
    """
    handles sorting part of quick sort. start and end points
    to first and last element of the array respectively
    """

    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses end pointer, 
    # and when it does, swaps the pivot with element on end pointer
    while start < end:
        # Increment the start pointer till it finds an element 
        # greater than pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an element
        # greter than pivot
        while array[end] > pivot:
            end -= 1
        
        # if start and end have not crossed  each other,
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
        
    # swap pivot element with element on end pointer
    # this puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # return end pointer to divide the array into 2
    return end


def quick_sort(start, end, array):
    """
    the main function that implements quicksort
    """

    if start < end:
        # p is partitioning index, arra[p] is at right place
        p = partition(start, end, array)

        # sort elements before partition and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
    
    return array
import numpy as np

def pointlessSort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubbleSort(arr):
    if len(arr) <= 1: #if the array is empty or only one element, return
        return arr

    for i in range(len(arr)):
        for j in range((len(arr) - 1 - i)):
            first = arr[j]

            if first > arr[j+1]:
                arr[j] = arr[j+1]
                arr[j+1] = first
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for x in range(low, high):
        if arr[x] < pivot:
            arr[i],arr[x] = arr[x],arr[i]
            i = i + 1

    arr[i], arr[high] = arr[high], arr[i]

    return i

def quickSort_rec(arr, low, high):

    if low >= high:
        return
    else:
        p = partition(arr, low, high)
        quickSort_rec(arr,low,p-1)
        quickSort_rec(arr,p+1,high)

    return arr

def quickSort(arr):
    return quickSort_rec(arr, 0, len(arr) - 1)

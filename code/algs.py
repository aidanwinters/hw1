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

    conditionals = 1 # includes the above if statement
    assignments = 0

    for i in range(len(arr)):
        assignments += 1 #for the above loop
        conditionals += 1 # for the above loop

        for j in range((len(arr) - 1 - i)):
            assignments += 1 #for the above loop
            conditionals += 1 # for the above loop

            first = arr[j]
            assignments += 1 # one assignment to hold current value

            if first > arr[j+1]:
                arr[j] = arr[j+1]
                arr[j+1] = first
                assignments += 2 #adding two assignments for the switch

            conditionals += 1 # for the above if statement
    return arr, conditionals, assignments

def insertionSort(arr):
    if len(arr) <= 1: #if the array is empty or only one element, return
        return arr

    conditionals = 1 # includes the above if statement
    assignments = 0

    for i in range(1, len(arr)):
        assignments += 1 #for the above loop
        conditionals += 1 # for the above loop

        temp = arr[i]
        j = i-1
        assignments += 2 #for the counter and for storing current

        while j >= 0 and temp < arr[j]:
            conditionals += 2 # for the above loop

            arr[j+1] = arr[j]
            j = j - 1

            assignments += 2

        arr[j+1] = temp
        assignments += 1

    return arr, conditionals, assignments

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

    if len(arr) <= 1:
        return arr
    elif low >= high:
        return arr
    else:
        p = partition(arr, low, high)
        quickSort_rec(arr,low,p-1)
        quickSort_rec(arr,p+1,high)

    return arr

def quickSort(arr):
    return quickSort_rec(arr, 0, len(arr) - 1)

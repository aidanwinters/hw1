import numpy as np

def pointlessSort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubbleSort(arr):

    conditionals = 1 # includes the below if statement
    assignments = 0

    if len(arr) <= 1: #if the array is empty or only one element, return
        return arr, conditionals, assignments

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

    conditionals = 1 # includes the below if statement
    assignments = 0

    if len(arr) <= 1: #if the array is empty or only one element, return
        return arr, conditionals, assignments

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

    conds = 2 #for the above 2 assignments
    assigns = 0

    for x in range(low, high):
        conds += 1 #for the above loop
        assigns += 1 #for the above loop
        if arr[x] < pivot:
            arr[i],arr[x] = arr[x],arr[i]
            i = i + 1
            assigns+=3 #2 for the swap, 1 for increment

        conds += 1 #for the above if statements

    arr[i], arr[high] = arr[high], arr[i]

    assigns += 2 # 2 for final swap

    return i, conds, assigns

def quickSort_rec(arr, low, high):

    conditionals = 1 # includes the below if statement
    assignments = 0

    if len(arr) <= 1: #if the array is empty or only one element, return
        return arr, conditionals, assignments
    elif low >= high:
        return arr, conditionals, assignments
    else:
        p,p_cond,p_assign = partition(arr, low, high)
        larr, lcond, lassign = quickSort_rec(arr,low,p-1)
        harr, hcond, hassign = quickSort_rec(arr,p+1,high)

        cc = conditionals +  p_cond + lcond + hcond
        aa = assignments +  p_assign + lassign + hassign

    return arr, cc, aa

def quickSort(arr):
    return quickSort_rec(arr, 0, len(arr) - 1)

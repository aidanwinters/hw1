# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quickSort, insertionSort, bubbleSort
from timeit import default_timer as timer
import matplotlib.pyplot as plt

def run_stuff():
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)

    x = np.random.rand(10)
    print("Unsorted input: ", x)

    print("Bubble sort output: ", bubbleSort(x))
    print("Insertion sort output: ", insertionSort(x))
    print("Quick sort output: ", quickSort(x))

def time_algos(num_reps = 100, steps = range(100,1100, 100)):

    sizes = []
    bub = []
    insert = []
    quick = []

    for i in steps:
        for j in range(num_reps):
            ran_arr = np.random.randint(i, size=i)
            start = timer()
            bubbleSort(ran_arr)
            mid1 = timer()
            insertionSort(ran_arr)
            mid2 = timer()
            quickSort(ran_arr)
            end = timer()

            sizes.append(i)
            bub.append(mid1-start)
            insert.append(mid2-mid1)
            quick.append(end-mid2)

    plt.scatter(sizes, bub)
    plt.show()
    plt.scatter(sizes, insert)
    plt.show()
    plt.scatter(sizes, quick)
    plt.show()
    return sizes, bub, insert, quick

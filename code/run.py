# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quickSort, insertionSort, bubbleSort
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import math

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

def time_algos(num_reps = 2, steps = range(100,1100, 100)):

    sizes = []
    bubble = {'times':[], 'assigns':[], 'conds':[]}
    insert = {'times':[], 'assigns':[], 'conds':[]}
    quick = {'times':[], 'assigns':[], 'conds':[]}

    # ran_arr = np.random.randint(100, size=100)
    # arr, cc, aa = insertionSort(ran_arr)
    #
    # print(arr)
    # print(cc)
    # print(aa)

    # for i in steps:
    #     for j in range(num_reps):
    #         ran_arr = np.random.randint(i, size=i)
    #         ins, ic, ia = insertionSort(ran_arr)
    #
    # return None

    for i in steps:
        for j in range(num_reps):
            ran_arr = np.random.randint(i, size=i)
            start = timer()
            bub, bc, ba = bubbleSort(ran_arr)

            ran_arr = np.random.randint(i, size=i)
            mid1 = timer()
            ins, ic, ia = insertionSort(ran_arr)

            ran_arr = np.random.randint(i, size=i)
            mid2 = timer()
            qui, qc, qa = quickSort(ran_arr)
            end = timer()

            sizes.append(i)
            bubble['times'].append(mid1-start)
            insert['times'].append(mid2-mid1)
            quick['times'].append(end-mid2)

            bubble['conds'].append(bc)
            insert['conds'].append(ic)
            quick['conds'].append(qc)

            bubble['assigns'].append(ba)
            insert['assigns'].append(ia)
            quick['assigns'].append(qa)

    sizes = np.array(sizes)

    # plt.scatter(sizes, bubble['times'])
    # plt.scatter(sizes, quick['times'])
    # plt.scatter(sizes, insert['times'])
    # plt.title('Time')
    # plt.legend(['Bubble', 'Quick', 'Insertion'], loc='upper left')
    # plt.show()

    plt.plot(sizes, (sizes * np.log(sizes)))
    plt.plot(sizes, (sizes**2 ))
    plt.scatter(sizes, bubble['conds'])
    plt.scatter(sizes, quick['conds'])
    plt.scatter(sizes, insert['conds'])
    plt.title('Conditionals')
    plt.legend([ 'n*log(n)', 'n^2','Bubble', 'Quick', 'Insertion'], loc='upper left')
    plt.show()

    plt.scatter(sizes, bubble['assigns'])
    plt.scatter(sizes, quick['assigns'])
    plt.scatter(sizes, insert['assigns'])
    plt.title('Assignments')
    plt.legend(['Bubble', 'Quick', 'Insertion'], loc='upper left')
    plt.show()
    return sizes, bub, insert, quick

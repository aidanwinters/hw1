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

def time_algos(num_reps = 100, steps = range(100,1100, 100)):

    sizes = []
    bubble = {'times':[], 'assigns':[], 'conds':[]}
    insert = {'times':[], 'assigns':[], 'conds':[]}
    quick = {'times':[], 'assigns':[], 'conds':[]}

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
    # plt.xlabel('Size of Array')
    # plt.ylabel('Runtime (s)')
    # plt.show()

    # plt.plot(sizes, (sizes * np.log(sizes)))
    # plt.plot(sizes, (sizes**2 ))
    # plt.plot(sizes, 0.5*(sizes**2 ))
    # plt.scatter(sizes, bubble['conds'])
    # plt.scatter(sizes, quick['conds'])
    # plt.scatter(sizes, insert['conds'])
    # plt.title('Conditionals')
    # # plt.legend([ 'n*log(n)', 'n^2', '0.5 * n^2', 'Bubble', 'Quick', 'Insertion'], loc='upper left')
    # plt.legend(['Bubble', 'Quick', 'Insertion'], loc='upper left')
    # plt.xlabel('Size of Array')
    # plt.ylabel('# of Conditionals')
    # plt.show()

    # plt.plot(sizes, (sizes * np.log(sizes)))
    # plt.plot(sizes, (sizes**2 ))
    # plt.plot(sizes, 0.5*(sizes**2 ))
    # plt.scatter(sizes, bubble['assigns'])
    # plt.scatter(sizes, quick['assigns'])
    # plt.scatter(sizes, insert['assigns'])
    # plt.title('Assignments')
    # # plt.legend(['n*log(n)', 'n^2', '0.5 * n^2', 'Bubble', 'Quick', 'Insertion'], loc='upper left')
    # plt.legend(['Bubble', 'Quick', 'Insertion'], loc='upper left')
    # plt.xlabel('Size of Array')
    # plt.ylabel('# of Assignments')
    # plt.show()

    # plt.plot(sizes, (sizes**2 ))
    # plt.scatter(sizes, bubble['conds'])
    # plt.xlabel('Size of Array')
    # plt.ylabel('# of Conditionals')
    # plt.legend(['n^2', 'Bubble'], loc='upper left')
    # plt.show()
    # plt.plot(sizes, 1.5 * (sizes**2 ))
    # plt.scatter(sizes, bubble['assigns'])
    # plt.xlabel('Size of Array')
    # plt.ylabel('# of Assignments')
    # plt.legend(['1.5 * (n^2)', 'Bubble'], loc='upper left')
    # plt.show()
    #
    # plt.plot(sizes, 0.5*(sizes**2 ))
    # plt.scatter(sizes, insert['conds'])
    # plt.xlabel('Size of Array')
    # plt.ylabel('# of Conditionals')
    # plt.legend(['0.5 * n^2', 'Insert'], loc='upper left')
    # plt.show()
    # plt.plot(sizes, 0.5*(sizes**2 ))
    # plt.scatter(sizes, insert['assigns'])
    # plt.xlabel('Size of Array')
    # plt.ylabel('# of Assignments')
    # plt.legend(['0.5 * n^2', 'Insert'], loc='upper left')
    # plt.show()

    plt.plot(sizes, 4*(sizes * np.log(sizes)))
    plt.scatter(sizes, quick['conds'])
    plt.xlabel('Size of Array')
    plt.ylabel('# of Conditionals')
    plt.legend(['4 (n log(n))', 'Quick'], loc='upper left')
    plt.show()
    plt.plot(sizes, 4*(sizes * np.log(sizes)))
    plt.scatter(sizes, quick['assigns'])
    plt.xlabel('Size of Array')
    plt.ylabel('# of Assignments')
    plt.legend(['4 (n log(n))', 'Quick'], loc='upper left')
    plt.show()

    return sizes, bub, insert, quick

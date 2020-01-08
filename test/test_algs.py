import numpy as np
from code import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointlessSort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointlessSort(x), np.array([1,2,3]))

def test_bubblesort():

    x = np.array([1,2,4,0,1])

    assert np.array_equal(algs.bubbleSort([]), []) #EMPTY ARRAY
    assert np.array_equal(algs.bubbleSort([1]), [1]) #ARRAY OF ONE
    assert np.array_equal(algs.bubbleSort(x), sorted(x)) #SORT ACTUAL ARRAY

    x = np.array([1,1,1,1,1])
    assert np.array_equal(algs.bubbleSort(x), sorted(x)) #TEST DUPLICATES


def test_quicksort():

    x = np.array([1,2,4,0,1])
    # for now, just attempt to call the quicksort function, should
    # actually check output
    algs.quickSort(x)

def sort(array):
    p = 0
    r = len(array)-1
    quickSort(array, p ,r)


def quickSort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quickSort(array, p, q-1)
        quickSort(array, q+1, r)


def partition(array, p, r):
    pivot = array[r]
    smaller = p
    for i in range(p, r):
        if array[i] <= pivot:
            array[smaller], array[i] = array[i], array[smaller]
            smaller = smaller + 1
    array[smaller], array[r] = array[r], array[smaller]
    return smaller

def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q-1)
        quick_sort(array, q+1, r)


def partition(array, p, r):
    pivot = array[r]
    smaller = p
    for i in range(p, r):
        if array[i] <= pivot:
            array[smaller], array[i] = array[i], array[smaller]
            smaller = smaller + 1
    array[smaller], array[r] = array[r], array[smaller]



    return smaller

array = [4, 8, 27, 5, 4, 57, 1, 23, 9, 5, 8, 22, 6, 12, 100]
 

quick_sort(array, 0, len(array) - 1)
print(array)

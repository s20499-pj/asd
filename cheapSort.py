heap = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
l=len(heap)-1


def maxHeapify(a: array, l: int, i: int):
    largest = i
    leftChild = 2*i+1
    rightChild = 2*i+2

    if leftChild < l and a[leftChild] > a[i]:
        largest = leftChild

    if rightChild < l and a[rightChild] > a[largest]:
        largest = rightChild

    if i != largest:
        a[i], a[largest] = a[largest], a[i]
        maxHeapify(a, l, largest)


def buildMaxHeap(a: array):
    for i in range((l//2), -1, -1):
        maxHeapify(a, l, i)


def heapSort(a: array):
    buildMaxHeap(a)
    for i in range(l, 0, -1):
        a[i], a[0] = a[0], a[i]
        maxHeapify(a, i,  0)


heapSort(heap)
print(heap)

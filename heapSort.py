def sort(array):
    arr = array
    heapSort(arr)


def maxHeapify(arr, l: int, i: int):
    largest = i
    leftChild = 2*i+1
    rightChild = 2*i+2

    if leftChild < l and arr[leftChild] > arr[i]:
        largest = leftChild

    if rightChild < l and arr[rightChild] > arr[largest]:
        largest = rightChild

    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, l, largest)


def buildMaxHeap(arr):
    l=len(arr)-1
    for i in range((l//2), -1, -1):
        maxHeapify(arr, l, i)



def heapSort(arr):
    buildMaxHeap(arr)
    l=len(arr)-1
    for i in range(l, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

        maxHeapify(arr, i, 0)

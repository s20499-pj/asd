import time
import quickSort
import heapSort
import margeSort
import inputs
import sys
sys.setrecursionlimit(1500)


print("1000 elements random array")
a = inputs.iooo.copy()
start = time.time()
quickSort.sort(a)
end = time.time()
print("Quick sort:  ", (end - start)*1000, "ms")

a = inputs.iooo.copy()
start = time.time()
heapSort.sort(a)
end = time.time()
print("Heap Sort:   ", (end - start)*1000, "ms")

a = inputs.iooo.copy()
start = time.time()
margeSort.sort(a)
end = time.time()
print("Marege Sort: ", (end - start)*1000, "ms")
print("---------------------------")

print("1000 elements sorted array")
a = inputs.ioooSorted.copy()
start = time.time()
quickSort.sort(a)
end = time.time()
print("Quick sort:  ", (end - start)*1000, "ms")

a = inputs.ioooSorted.copy()
start = time.time()
heapSort.sort(a)
end = time.time()
print("Heap Sort:   ", (end - start)*1000, "ms")

a = inputs.ioooSorted.copy()
start = time.time()
margeSort.sort(a)
end = time.time()
print("Marege Sort: ", (end - start)*1000, "ms")
print("---------------------------")

print("1000 elements reverse sorted array")
a = inputs.ioooReverse.copy()
start = time.time()
quickSort.sort(a)
end = time.time()
print("Quick sort:  ", (end - start)*1000, "ms")

a = inputs.ioooReverse.copy()
start = time.time()
heapSort.sort(a)
end = time.time()
print("Heap Sort:   ", (end - start)*1000, "ms")

a = inputs.ioooReverse.copy()
start = time.time()
margeSort.sort(a)
end = time.time()
print("Marege Sort: ", (end - start)*1000, "ms")
print("---------------------------")

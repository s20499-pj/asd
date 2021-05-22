import time
import quickSort
import heapSort
import margeSort
import inputs
import sys
sys.setrecursionlimit(50000)

print("50k elements random array")
a = inputs.sok.copy()
start = time.time()
quickSort.sort(a)
end = time.time()
print("Quick sort:  ", (end - start)*1000, "ms")

a = inputs.sok.copy()
start = time.time()
heapSort.sort(a)
end = time.time()
print("Heap Sort:   ", (end - start)*1000, "ms")

a = inputs.sok.copy()
start = time.time()
margeSort.sort(a)
end = time.time()
print("Marege Sort: ", (end - start)*1000, "ms")
print("---------------------------")

print("50k elements sorted array")
a = inputs.sokSort.copy()
start = time.time()
#quickSort.sort(a)
end = time.time()
print("Quick sort:  MEMORY DUMP", (end - start)*1000, "ms")

a = inputs.sokSort.copy()
start = time.time()
heapSort.sort(a)
end = time.time()
print("Heap Sort:   ", (end - start)*1000, "ms")

a = inputs.sokSort.copy()
start = time.time()
margeSort.sort(a)
end = time.time()
print("Marege Sort: ", (end - start)*1000, "ms")
print("---------------------------")

print("50k elements reverse sorted array")
a = inputs.sokRev.copy()
start = time.time()
quickSort.sort(a)
end = time.time()
print("Quick sort:  ", (end - start)*1000, "ms")

a = inputs.sokRev.copy()
start = time.time()
heapSort.sort(a)
end = time.time()
print("Heap Sort:   ", (end - start)*1000, "ms")

a = inputs.sokRev.copy()
start = time.time()
margeSort.sort(a)
end = time.time()
print("Marege Sort: ", (end - start)*1000, "ms")
print("---------------------------")

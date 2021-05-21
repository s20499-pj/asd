import time
import quickSort
import heapSort
import margeSort
import inputs


print("10 elements array")
a = inputs.io.copy()
start = time.time()
quickSort.sort(a)
end = time.time()
print("Quick sort: ", end - start)

a = inputs.io.copy()
start = time.time()
heapSort.sort(a)
end = time.time()
print("Heap Sort: ", end - start)

a = inputs.io.copy()
start = time.time()
margeSort.sort(a)
end = time.time()
print("Marege Sort: ", end - start)
print("---------------------------")

print("100 elements array")
a = inputs.ioo.copy()
start = time.time()
quickSort.sort(a)
end = time.time()
print("Quick sort: ", end - start)

a = inputs.ioo.copy()
start = time.time()
heapSort.sort(a)
end = time.time()
print("Heap Sort: ", end - start)

a = inputs.ioo.copy()
start = time.time()
#margeSort.sort(a)
end = time.time()
print("Marege Sort: ", end - start)
print("---------------------------")

print("1000 elements array")
a = inputs.iooo.copy()
start = time.time()
quickSort.sort(a)
end = time.time()
print("Quick sort: ", end - start)

a = inputs.iooo.copy()
start = time.time()
heapSort.sort(a)
end = time.time()
print("Heap Sort: ", end - start)

a = inputs.iooo.copy()
start = time.time()
#margeSort.sort(a)
end = time.time()
print("Marege Sort: ", end - start)
print("---------------------------")

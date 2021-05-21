def sort(arr):
    maxele = max(arr) + 1
    mergeSortRec(arr, 0, len(arr)-1, maxele)

def mergeSortRec(arr, beg, end, maxele):
    if (beg < end):
        mid = (beg + end) // 2
        mergeSortRec(arr, beg, mid, maxele)
        mergeSortRec(arr, mid + 1, end, maxele)
        merge(arr, beg, mid, end, maxele)


def merge(arr, beg, mid, end, maxele):
    #left side of marge array
    i = beg
    #rigt side of marge array
    j = mid + 1
    #pointer to new place
    k = beg
    #print("")
    while (i <= mid and j <= end):
        """print('compare',
              arr[i] % maxele,
              arr[j] % maxele,
              'and put in k',
              arr[k])
        print(arr)"""
        if (arr[i] % maxele <= arr[j] % maxele):
            arr[k] = arr[k] + (arr[i] % maxele) * maxele
            k += 1
            i += 1
        else:
            arr[k] = arr[k] + (arr[j] % maxele) * maxele
            k += 1
            j += 1

    while (i <= mid):
        arr[k] = arr[k] + (arr[i] % maxele) * maxele
        k += 1
        i += 1

    while (j <= end):
        arr[k] = arr[k] + (arr[j] % maxele) * maxele
        k += 1
        j += 1

    for i in range(beg, end + 1):
        arr[i] = arr[i] // maxele

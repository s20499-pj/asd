def sort(arr):
    binaryelSort(arr)
    
def binaryelSort(arr):
    ofl = 0          #offset left
    ofr = len(arr)-1 #offset right
    maxele = max(arr)
    while (ofl <= ofr):
        if (arr[ofl]<maxele):
            ofl +=1
        else:
            arr[ofl], arr[ofr] = arr[ofr], arr[ofl]
            ofr -=1

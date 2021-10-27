def merge(A, temp, frm, mid, to):
 
    k = frm
    i = frm
    j = mid + 1
 
    # loop till no elements are left in the left and right runs
    while i <= mid and j <= to:
        yield A, i, j, frm, to
        if A[i] < A[j]:
            temp[k] = A[i]
            i = i + 1
        else:
            temp[k] = A[j]
            j = j + 1
 
        k = k + 1
 
    # copy remaining elements
    while i < len(A) and i <= mid:
        yield A, i, j, frm, to
        temp[k] = A[i]
        k = k + 1
        i = i + 1
 
    ''' no need to copy the second half (since the remaining items
        are already in their correct position in the temporary array) '''
 
    # copy back to the original list to reflect sorted order
    for i in range(frm, to + 1):
        #yield A, i, i, frm, to
        A[i] = temp[i]
 
 
# Iteratively sort sublist `A[low…high]` using a temporary list
def iterativemergeSort(A, *args):
 
    low = 0
    high = len(A) - 1
 
    # sort list `A` using a temporary list `temp`
    temp = A.copy()
 
    # divide the list into blocks of size `m`
    # m = [1, 2, 4, 8, 16…]
 
    m = 1
    while m <= high - low:
 
        # for m = 1, i = [0, 2, 4, 6, 8…]
        # for m = 2, i = [0, 4, 8, 12…]
        # for m = 4, i = [0, 8, 16…]
        # …
 
        for i in range(low, high, 2*m):
            frm = i
            mid = i + m - 1
            to = min(i + 2*m - 1, high)
            yield from merge(A, temp, frm, mid, to)
 
        m = 2*m
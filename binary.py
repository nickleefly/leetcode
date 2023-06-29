def maxInBitonic(arr, l, r):
    while (l <= r):
        m = int(l + (r - 1)/2)

        if ((r == l + 1) and arr[l] >= arr[r]):
            return arr[l]
        if ((r == l + 1) and arr[l] < arr[r]):
            return arr[r]
        if (arr[m] > arr[m + 1] and arr[m] > arr[m - 1]):
            return arr[m]
        if (arr[m] > arr[m + 1] and arr[m] < arr[m - 1]):
            # move left with l and r = m -1
            r = m - 1
        else:
            # move right with l = m + 1 and r
            l = m + 1
    # if we return here, then element was not present
    return -1

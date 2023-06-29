def partition(self, A, start, end):
    # patition in quicksort
    if start >= end:
        return
    left, right = start, end

    # key point 1: pivot is the value, not the index
    pivot = A[(start + end) // 2]
    # key point 2: every time you compare left & right, it should be
    # left <= right not left < right

    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1


def merge(list1, list2):
    new_list = []
    i, j = 0, 0
    # move i, j in merge process, dont use list1.pop(0)
    # pop(0) is O(n)
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    # merge remaining to new_list
    # dont use new_list.extend(list1[i:]), it causes more space operation
    while i < len(list1):
        new_list.append(list1[i])
        i += 1
    while j < len(list2):
        new_list.append(list2[j])
        j += 1
    return new_list

from typing import List


def sortColors(nums):
    # initialize indices to partition the array
    left, right = 0, len(nums) - 1
    # initialize index to iterate through the array
    i = 0
    # loop through the array
    while i <= right:
        # if the current element is 0, swap it with the leftmost element and move leftwards by 1
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        # if the current element is 2, swap it with the rightmost element and move rightwards by 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        # if the current element is 1, don't swap and move to the next element
        else:
            i += 1
    return nums


def sort_colors(nums):
    # Define a recursive helper function to perform quicksort in-place
    def quicksort(left, right):
        # Divide the array into two partitions using a pivot element
        pivot = nums[(left + right) // 2]
        i, j = left, right
        while i <= j:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        # Recursively call quicksort on the two partitions
        if left < j:
            quicksort(left, j)
        if i < right:
            quicksort(i, right)

    # Call quicksort on the entire array
    quicksort(0, len(nums) - 1)


class SolutionMergeSort:
    def sortColors(self, nums: List[int]) -> None:
        # Define a recursive helper function to perform merge sort in-place
        def mergesort(left, right):
            if left < right:
                mid = (left + right) // 2
                mergesort(left, mid)
                mergesort(mid + 1, right)

                # Merge the two sorted sub-arrays
                i, j = left, mid + 1
                while i <= mid and j <= right:
                    if nums[i] < nums[j]:
                        i += 1
                    else:
                        tmp = nums[j]
                        for k in range(j, i-1, -1):
                            nums[k] = nums[k - 1]
                        nums[i] = tmp
                        i += 1
                        mid += 1
                        j += 1

        # Call mergesort on the entire array
        mergesort(0, len(nums) - 1)


class SolutionHeapsort:
    def sortColors(self, nums: List[int]) -> None:
        # Define a helper function to maintain the heap property
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[l] > arr[largest]:
                largest = l

            if r < n and arr[r] > arr[largest]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        # Build a max-heap from the given array
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

        # Extract elements from the heap one at a time to build the sorted array
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))

"""
The time and space complexities for merge sort, quicksort, and heapsort are as follows:

### Merge Sort

- Time Complexity: O(n log n) in the worst, average, and best cases.
- Space Complexity: O(n) in the worst case, since we need to allocate space for temporary arrays during the merging phase.

### Quicksort

- Time Complexity: O(n log n) in the average and best cases, but O(n^2) in the worst case when the pivot divides the array into two sub-arrays of size 0 and n-1, respectively.
- Space Complexity: O(log n) in the average case due to the recursive calls required, but O(n) in the worst case due to the recursion stack.

### Heapsort

- Time Complexity: O(n log n) in all cases, since that's the cost of building a binary heap and removing the root n times.
- Space Complexity: O(1) in the worst case, since in-place heap sorting doesn't need extra space except for variable allocations.

Overall, all three algorithms have a worst-case time complexity of O(n log n) and are efficient for large datasets. However, merge sort and heapsort are more space-efficient than
quicksort in the worst-case scenario. QuickSort is often faster in practice because it has a smaller constant factor and has good cache locality due to its in-place nature.
Heapsort is generally the slowest out of the three algorithms, though its main advantage is its guaranteed worst-case time complexity of O(n log n).
"""

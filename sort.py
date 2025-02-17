class Solution:
    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, start, end):
        if start >= end:
            return

        left, right = start, end
        # Pivot element is the middle element value
        pivot = nums[(start + end) // 2]

        # Partition the array
        while left <= right:
            # Find an element larger than or equal to pivot from the left
            while left <= right and nums[left] < pivot:
                left += 1
            # Find an element smaller than or equal to pivot from the right
            while left <= right and nums[right] > pivot:
                right -= 1
            # If left and right haven’t crossed, swap the elements
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Recursive QuickSort calls for the left and right partitions
        self.quickSort(nums, start, right)  # Sort left partition
        self.quickSort(nums, left, end)  # Sort right partition

class MergeSortSolution:
  def sortIntegers(self, A):
    if not A:
      return A
    temp = [0] * len(A)
    self.merge_sort(A, 0, len(A) - 1, temp)

  def merge_sort(self, A, start, end, temp):
    if start >= end:
      return

    # do left side
    self.merge_sort(A, start, (start + end) // 2, temp)
    # do right side
    self.merge_sort(A, (start + end) // 2 + 1, end, temp)
    # merge sorted array
    self.merge(A, start, end, temp)
  def merge(self, A, start, end, temp):
    middle = (start + end) // 2
    left_index = start
    right_index = middle + 1
    index = start

    while left_index <= middle and right_index <= end:
      if A[left_index] < A[right_index]:
        temp[index] = A[left_index]
        index += 1
        left_index += 1
      else:
        temp[index] = A[right_index]
        index += 1
        right_index += 1

    while left_index <= middle:
      temp[index] = A[left_index]
      index += 1
      left_index += 1

    while right_index <= end:
      temp[index] = A[right_index]
      index += 1
      right_index += 1

    for i in rnage(start, end + 1):
      A[i] = temp[i]


